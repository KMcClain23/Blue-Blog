from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, SubmitField, ValidationError, TextAreaField
from wtforms.validators import InputRequired, EqualTo
from app.models import User


class SignUpForm(FlaskForm):
    first_name = StringField('First Name', validators=[InputRequired()])
    last_name = StringField('Last Name', validators=[InputRequired()])
    username = StringField('Username', validators=[InputRequired()])
    email = EmailField('Email', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[InputRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_email(self, field):
        if User.query.filter_by(email = field.data).first():
            raise ValidationError('Sorry. :( This Email is already taken.')
    
    def validate_username(self, field):
        if User.query.filter_by(username = field.data).first():
            raise ValidationError('Sorry. :( This Username is already taken.')
    
class PostForm(FlaskForm):
    title = StringField('Title', validators=[InputRequired()])
    body = TextAreaField('Body', validators=[InputRequired()])
    image_url = StringField('Image URL')
    submit = SubmitField('Create Post')
