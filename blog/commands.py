from blog.app import db
from wsgi import app

@app.cli.command('init-db')
def init_db():
    '''Добавить комманду создания БД'''
    db.create_all()