
from flask import session, redirect, url_for
from flask_babel import Babel
from flask_admin import Admin, AdminIndexView
from flask_admin.contrib.sqla import ModelView

from loja.ext.database import db
from loja.model import Product


class AdminProtegido(AdminIndexView):

    def is_accessible(self):
        return session.get("admin_logado", False)

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for("webui.login"))


class ProdutoProtegido(ModelView):

    def is_accessible(self):
        return session.get("admin_logado", False)

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for("webui.login"))


def init_app(app):
    babel = Babel(app)

    admin = Admin(
        app,
        index_view=AdminProtegido()
    )

    admin.add_view(ProdutoProtegido(Product, db.session))
