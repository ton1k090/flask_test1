from werkzeug.security import generate_password_hash

from blog.app import create_app, db


app = create_app()

@app.cli.command("init-db")
def init_db():
    '''Создать базу данных'''
    db.create_all()


@app.cli.command("create-users")
def create_users():
    '''create superusers создать пользователя'''
    from blog.models import User
    db.session.add(
        User(email="name@email.com", password=generate_password_hash("test"))
    )
    db.session.commit()