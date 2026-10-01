from loja.ext.database import db
from loja.model import Product
from flask_babel import Babel
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

def init_app(app):
    babel = Babel(app)
    admin = Admin(app)
    admin.add_view(ModelView(Product, db.session))
