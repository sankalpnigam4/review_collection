from flask_wtf import Form, RecaptchaField
from wtforms import TextField, PasswordField, TextAreaField, StringField, validators


class RegisterForm(Form):
    name = StringField('name', [validators.DataRequired()])
    email = StringField('email', [validators.DataRequired()])
    rating = StringField('rating',  [validators.DataRequired()])
    website = StringField('website')
    review = StringField('review')
    recaptcha = RecaptchaField()
