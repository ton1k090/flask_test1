from flask_wtf import FlaskForm
from wtforms import StringField, validators, PasswordField, SubmitField


class UserRegisterForm(FlaskForm):
    '''Форма регистрации пользователя с валидаторами'''
    first_name = StringField('First Name')
    last_name = StringField('Last Name')
    email = StringField('E-mail', [validators.DataRequired(), validators.Email()]) # Строка с валидаторами
    password = PasswordField('Password', [validators.DataRequired(), validators.EqualTo('confirm_password', message='Passwords must match')])
    confirm_password = PasswordField('Confirm Password', [validators.DataRequired()])
    submit = SubmitField('Register')