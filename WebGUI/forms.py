from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField, IntegerField, FloatField
from wtforms.validators import DataRequired, InputRequired, Email, Length #data required validates imputs in submit

def validate_gen(form, field):
    if (field.data !=  'male') and (field.data !=  'female'):
        raise ValidationError('please enter either male or female')
def bday(form, field):
    a = field.data
    if (a[2] != '/' or a[5] != '/'):
        raise ValidationError('please enter either male or female')

class SignupFrom(Form):
    first_name = StringField('First Name', validators=[DataRequired("Please enter your first name")])
    last_name = StringField('Last Name',validators=[DataRequired("Please enter your last name")])
    email = StringField('Email',validators=[DataRequired("Please enter a valid email"), Email("Please enter a valid email")])
    password = PasswordField('Password',validators=[DataRequired("Please enter a password"),Length(min=6, message="Passwords must be atleast 6 characters long")])
    sex = StringField('Gender',validators=[DataRequired("Please enter a gender"),validate_gen])
    birthday = StringField('Birthday', validators=[DataRequired("Please enter a Date in the form mm/dd/yyyy"),bday])
    orientation = StringField('Preference', validators=[DataRequired("Please enter who you are looking for"),validate_gen])
    address = StringField('Location', validators=[DataRequired("Please enter a valid address or location")])
    submit = SubmitField('Sign up')

class LoginForm(Form):
    email = StringField('Email', validators=[DataRequired("Please enter your email address."), Email("Please enter your email address.")])
    password = PasswordField('Password', validators=[DataRequired("Please enter a password")])
    submit = SubmitField("Sign in")

class AddressForm(Form):
  address = StringField('Location', validators=[DataRequired("Please enter a valid address or location")])
  submit = SubmitField("Search")
