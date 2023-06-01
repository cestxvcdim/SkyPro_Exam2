from flask import Flask
from flask_restx import Api
from configs.default_config import Config
from setup_db import db
from views.lectures import lecture_ns


def create_app(config: Config) -> Flask:
    """
    Create an application
    And apply all configurations
    With extensions.

    Returns the application.
    """
    application = Flask(__name__)
    application.config.from_object(config)
    application.app_context().push()
    register_extensions(application)
    return application


def register_extensions(application: Flask) -> None:
    """
    Initialize a database for the application.

    Create the api for application
    And add all namespaces.
    """

    db.init_app(application)
    api = Api(application)
    api.add_namespace(lecture_ns)


app_config = Config()
app = create_app(app_config)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run()
