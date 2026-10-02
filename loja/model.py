from sqlalchemy import Float, Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy_serializer import SerializerMixin
from werkzeug.security import check_password_hash, generate_password_hash

from loja.ext.database import db


class Product(db.Model, SerializerMixin):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=True)
    description: Mapped[str] = mapped_column(String(255), unique=True)
    price: Mapped[float] = mapped_column(Float)


class User(db.Model, SerializerMixin):
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(80), unique=True)
    passwordHash: Mapped[str] = mapped_column(String(255))

    def set_password(self, password):
        self.passwordHash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.passwordHash, password)


def populate_db():
    products = [
        Product(id=1, name="Resistor 470 ohms", description="Resistor de filme de carbono 470R 1/4W", price=0.05),
        Product(id=2, name="Arduino Nano R3", description="Placa de desenvolvimento microcontrolada ATmega328P", price=50.00),
        Product(id=3, name="Raspberry Pi 3", description="Single board computer ARM Cortex-A53 1.2GHz 1GB RAM", price=200.00),
    ]

    for product in products:
        if not Product.query.get(product.id):
            db.session.add(product)

    if not User.query.filter_by(username="admin").first():
        admin = User(username="admin")
        admin.set_password("admin123")
        db.session.add(admin)

    db.session.commit()