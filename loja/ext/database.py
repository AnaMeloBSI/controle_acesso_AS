from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Float, Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy_serializer import SerializerMixin


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)


def init_app(app):
    db.init_app(app)

    with app.app_context():
       
        db.create_all()
        
    
        from loja.model import Product, populate_db
        if not Product.query.first():
            populate_db()