from flask import Blueprint, render_template, redirect
from werkzeug.exceptions import NotFound
from flask_login import login_required


user = Blueprint('user', __name__, url_prefix='/users', static_folder='../static', template_folder='../templates')

# USERS = ['Alice', 'John', 'Mike']

USERS = {
    1: 'Alice',
    2: 'John',
    3: 'Mike',
}


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