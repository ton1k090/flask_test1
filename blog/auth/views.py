from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import logout_user, login_user, login_required
from werkzeug.security import check_password_hash


auth = Blueprint('auth', __name__, static_folder='../static')


@auth.route("/login", methods=["GET", "POST"]) # Поддерживает методы гет и пост
def login():
    '''Функция авторизации'''
    if request.method == "GET":
        return render_template(
            "auth/login.html"
        )
    from ..models import User

    email = request.form.get("email") # Получить из формы емейл ( неймы в шаблоне )
    password = request.form.get("password") # Получить из формы пароль ( неймы в шаблоне )
    user = User.query.filter_by(email=email).first() # Найти пользователя в БД по емейлу

    if not user or not check_password_hash(user.password, password): # Если пароль не верный или нет юзера
        flash("Check your login details") # Отправить сообщение на фронтенд
        return redirect(url_for(".login")) # Перенаправить на страницу логин снова
    login_user(user) #
    return redirect(url_for("user.profile", pk=user.id)) # Перенаправить на страницу профиль


@auth.route("/logout")
@login_required
def logout():
    '''Функция выход'''
    logout_user() #
    return redirect(url_for(".login"))