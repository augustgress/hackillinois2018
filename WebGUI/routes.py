import logging
import os
from flask import Flask, render_template, request, session, redirect, url_for #import class and function
from models import db, User, Place #import db variable
from forms import SignupFrom, LoginForm, AddressForm, BudgetForm
from google.cloud import storage
app = Flask(__name__) #creates instance of flask class

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://localhost/hackillinois2018' #used to attach database to application look at flasksqlalchemy page for more info
CLOUD_STORAGE_BUCKET = os.environ['gs://userpictures1']
db.init_app(app) #initialize app to use this setup

app.secret_key = "development-key" #protects against XSS

@app.route("/") #map this slash to the function index
def index():
    return render_template("index.html") #flask function renders index.html

@app.route("/about") #url for about page
def about():
    return render_template("about.html")

@app.route("/signup", methods=['GET','POST']) # renders signup page using routes
def signup():
    if 'email' in session:
        return redirect(url_for('home'))
    form = SignupFrom()
    temp = 0
    if request.method == 'POST':
        if form.validate() == False:
            return render_template('signup.html', form=form, temp = temp)
        else:
            email = form.email.data
            user = User.query.filter_by(email=email).first()

            if user is not None:
                temp = 1
                return render_template('signup.html', form=form, temp = temp)
            else:
                temp = 0
                newuser = User(form.first_name.data, form.last_name.data, form.email.data, form.password.data)
                db.session.add(newuser)
                db.session.commit()

                session['email'] = newuser.email #sets email for session object
                return redirect(url_for('image'))

    elif request.method == 'GET':
        return render_template('signup.html',form = form, temp = temp)
@app.route('/image')
def get():
        return """
<form method="POST" action="/upload" enctype="multipart/form-data">
    <input type="file" name="file">
    <input type="submit">
</form>
"""

@app.route('/upload', methods=['POST'])
def upload():
    """Process the uploaded file and upload it to Google Cloud Storage."""
    uploaded_file = request.files.get('file')

    if not uploaded_file:
        return 'No file uploaded.', 400

    # Create a Cloud Storage client.
    gcs = storage.Client()

    # Get the bucket that the file will be uploaded to.
    bucket = gcs.get_bucket(CLOUD_STORAGE_BUCKET)

    # Create a new blob and upload the file's content.
    blob = bucket.blob(uploaded_file.filename)

    blob.upload_from_string(
        uploaded_file.read(),
        content_type=uploaded_file.content_type
    )

    # The public URL can be used to directly access the uploaded file via HTTP.
    return blob.public_url

@app.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during a request.')
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500

@app.route("/login", methods=["GET","POST"]) #routing to login page
def login():
    if 'email' in session:
        return redirect(url_for('home'))
    form = LoginForm() #creates form object

    if request.method == "POST":
        if form.validate() == False: #redirects to same page if failed
            return render_template("login.html", form=form)
        else:
            email = form.email.data
            password = form.password.data

            user = User.query.filter_by(email=email).first()
            if user is not None and user.check_password(password):
                session['email'] = form.email.data #sets email for session object
                return redirect(url_for('home'))
            else:
                return redirect(url_for('login'))
    elif request.method == 'GET':
        return render_template('login.html', form=form)

@app.route("/logout") #pops session which is same as logging out
def logout():
    session.pop('email', None)
    return redirect(url_for('index'))

@app.route("/home", methods=["GET","POST"]) #private logged in page
def home():
    if 'email' not in session: #checks to see if logged in or not
        return redirect(url_for('login'))

    form = AddressForm()

    places = []
    my_coordinates = (41.7508, 88.1535)

    if request.method == 'POST':
      if form.validate() == False:
        my_coordinates = (41.7508, 88.1535)
        return render_template('home.html', form=form, my_coordinates=my_coordinates)
      else:
        # get the address
        address = form.address.data
        # query for places around it
        p = Place()
        my_coordinates = p.address_to_latlng(address)
        places = p.query(address)

        # return those results
        return render_template('home.html', form=form, my_coordinates=my_coordinates, places=places)

    elif request.method == 'GET':
      return render_template("home.html", form=form, my_coordinates=my_coordinates, places=places)

@app.route("/budget", methods=["GET","POST"])
def budget():
    if 'email' not in session: #checks to see if logged in or not
        return redirect(url_for('login'))

    form = BudgetForm()

    usable_money = 0
    food_estimate = 0
    daily_food = 0
    left = 0
    days = 0

    if request.method == "POST":
        if form.validate() == False: #redirects to same page if failed
            return render_template("budget.html", form=form, usable_money = usable_money, food_estimate = food_estimate, daily_food = daily_food, left = left, days = days)

        else:
            budget = form.budget.data
            days = form.days.data
            nights = form.nights.data
            hotel = form.hotel.data
            rental = form.cRental.data

            if days > 0 and nights > 0 and hotel > 0 and rental > 0:
                usable_money = budget-(hotel*nights)-(rental*days)
            elif days > 0 and rental > 0:
                usable_money = budget-(rental*days)
            elif nights > 0 and hotel > 0:
                usable_money = budget-(hotel*nights)
            else:
                usable_money = budget

            if days > 0:
                food_estimate = usable_money*.4
                daily_food = food_estimate/days


            left = usable_money-food_estimate

            return render_template('budget.html', form=form, usable_money = usable_money, food_estimate = food_estimate, daily_food = daily_food, left = left, days = days)

    elif request.method == 'GET':
      return render_template('budget.html', form=form, usable_money = usable_money, food_estimate = food_estimate, daily_food = daily_food, left = left, days = days)



if __name__ == "__main__":
    app.run(debug=True) #turns on debugging for the page
    app.run(host='127.0.0.1', port=8080, debug=True)
