
from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import login_required, current_user, login_user
from werkzeug.exceptions import NotFound
from werkzeug.security import generate_password_hash

from blog.extension import db
from blog.forms.user import UserRegisterForm
from blog.models import User

user = Blueprint('user', __name__, url_prefix='/users', static_folder='../static', template_folder='../templates')

# USERS = ['Alice', 'John', 'Mike']

USERS = {
    1: 'Alice',
    2: 'John',
    3: 'Mike',
}



@user.route('register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated: # Если юзер авторизован
        return redirect(url_for('user.profile', pk=current_user.id))

    form = UserRegisterForm(request.form) # Обращаемся к форме
    errors = [] # Список ошибок
    if request.method == 'POST' and form.validate_on_submit():
        if User.query.filter_by(email=form.email.data).count():
            form.email.errors.append('email already exists')
            return render_template('users/register.html', form=form)

        _user = User(
            email=form.email.data,
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            password=generate_password_hash(form.password.data),
        ) # Добавляем данные в БД

        db.session.add(_user) # Добавить юзера
        db.session.commit() # Коммит изменений

        login_user(_user) # Авторизовать

        return redirect(url_for('user.profile', pk=_user.id))

    return render_template(
        'users/register.html',
        form=form
    )


@user.route('/')
def user_list():
    from blog.models import User
    users = User.query.all() # Вернет весь список юзеров
    return render_template('users/list.html', users=users) # Рендер страницы и добавление данных


@user.route("/<int:pk>")
@login_required
def profile(pk: int):
    from ..models import User
    _user = User.query.filter_by(id=pk).one_or_none() # Либо вернет один элемент из списка либо ноне
    if _user is None:
        raise NotFound("User id:{}, not found".format(pk)) # Если юзер не найден
    return render_template(
        "users/profile.html",
        user=_user
    )