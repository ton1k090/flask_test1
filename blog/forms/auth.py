from flask_wtf import FlaskForm
from wtforms import StringField, validators, PasswordField, SubmitField


class AuthForm(FlaskForm):
    email = StringField('E-mail', [validators.DataRequired(), validators.Email()]) # Форма строка с валидаторами
    password = PasswordField('Password', [validators.DataRequired()]) # форма пароль с валидаторами
    submit = SubmitField('Login') # Кнопка