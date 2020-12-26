from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, Label
from wtforms.validators import DataRequired, Length, Email, EqualTo


class SearchForm(FlaskForm):
    search = StringField("Username", validators=[DataRequired()])
    submit = SubmitField("Search")


class CreateAccountForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    public_address = StringField("Your Public Address", validators=[DataRequired()])
    payment_address = Label("id", "")
    create_account = SubmitField("Create Account")


class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')