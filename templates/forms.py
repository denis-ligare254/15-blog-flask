from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField,BooleanField
from wtforms.validators import DataRequired, Length,Email,EqualTo



class RegistrationForm(FlaskForm):
    username=StringField('Username',validators=[DataRequired(),Length(min=2,max=20)])
    Email=StringField('Email',validators=[DataRequired(),Email()])
    password=PasswordField('password',validators=[DataRequired()])
    Confirm_password=PasswordField('confirm_password',validators=[DataRequired(),EqualTO("password")])
    submit =SubmitField('SignUp')



class LoginForm(FlaskForm):
    Email=StringField('Email',validators=[DataRequired(),Email()])
    password=PasswordField('password',validators=[DataRequired()])
    Remember_me=BooleanField('remember')
    submit =SubmitField('Login')