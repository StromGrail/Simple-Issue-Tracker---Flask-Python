from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from issuetracker import db

class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    FirstName = StringField('First Name',
                           validators=[DataRequired(), Length(min=2, max=20)])
    LastName = StringField('Last Name',
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


class PostIssueForm(FlaskForm):
    Title = StringField('Title',
                            validators = [ DataRequired(), Length(min=2, max=100)])
    Description = StringField('Description',
                            validators = [ DataRequired() ])
    AssignedTo = StringField('AssignedTo', 
                            validators = [ DataRequired() ])
    Createdby = StringField('Createdby',
                            validators = [ DataRequired() ])
    Status = BooleanField('Open Status' , default= True)
    submit = SubmitField('Post')

