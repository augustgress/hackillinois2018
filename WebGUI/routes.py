from flask import Flask, render_template, request, session, redirect, url_for #import class and function
from models import db, User, Place #import db variable
from forms import SignupFrom, LoginForm, AddressForm

app = Flask(__name__) #creates instance of flask class

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://localhost/hackillinois2018' #used to attach database to application look at flasksqlalchemy page for more info

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
                return redirect(url_for('home'))

    elif request.method == 'GET':
        return render_template('signup.html',form = form, temp = temp)

@app.route("/login", methods=["GET","POST"]) #routing to login page
def login():
    if 'email' in session:
        return redirect(url_for('budget'))
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
                return redirect(url_for('budget'))
            else:
                return redirect(url_for('index'))
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

    return redirect(url_for('budget'))

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
