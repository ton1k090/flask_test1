from blog.app import create_app


if __name__ == "__main__":
    '''Запустить приложение'''
    app = create_app()
    app.run()