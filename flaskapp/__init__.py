from flask import Flask
from flaskapp.config import Productoin, Development


# set "True" for Production
config_file = Productoin if True else Development


def create_app(config_file=config_file):
    # init flask
    app = Flask(__name__)
    app.config.from_object(config_file)

    # get blueprints
    from flaskapp.main import main
    from flaskapp.error import error

    # add blueprints app
    app.register_blueprint(main)
    app.register_blueprint(error)

    return app
