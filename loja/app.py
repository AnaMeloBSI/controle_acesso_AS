from flask import Flask
from loja.blueprints import restapi, webui
from loja.ext import admin, appearance, configuration, database


def create_app(**config):
    app = Flask(__name__)
    configuration.init_app(app, **config)
    database.init_app(app)
    appearance.init_app(app)
    admin.init_app(app)
    webui.init_app(app)
    restapi.init_app(app)

    return app