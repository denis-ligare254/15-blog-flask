from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length,Email,EqualTo



class RegestrationForm(FlaskForm):
    username=StringField('Username',validators=[DataRequired(),Length(min=2,max=20)])
    Email=StringField('Email',validators=[DataRequired(),Email()])
    password=StringField('password',validators=[DataRequired()])
    Confirm_password=StringField('confirm_password',validators=[DataRequired(),EqualTO("password")])