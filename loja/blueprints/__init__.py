from flask import Blueprint
from .views import index, product, login, logout

webui = Blueprint("webui", __name__)


def init_app(app):
    webui.add_url_rule("/", view_func=index)
    webui.add_url_rule("/product/", view_func=product)
    webui.add_url_rule("/login", view_func=login, methods=["GET", "POST"])
    webui.add_url_rule("/logout", view_func=logout)

    app.register_blueprint(webui)