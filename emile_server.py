from flask import Flask
import backend
from cruds.crud_aluno import views
import os


def create_app():
    app = Flask("emile")

    app.config.from_object(os.environ['APP_SETTINGS'])
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    backend.db.init_app(app)
    return app


app = create_app()
app.register_blueprint(views.user)

if __name__ == '__main__':
    app.run()
