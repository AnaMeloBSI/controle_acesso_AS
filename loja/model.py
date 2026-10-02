from loja.ext.database import db, SerializerMixin, mapped_column, Mapped
from werkzeug.security import generate_password_hash, check_password_hash



class Product(db.Model, SerializerMixin):
    id: Mapped[int] = mapped_column(primary_key=True)
    description: Mapped[str] = mapped_column(unique=True)
    price: Mapped[float]


class User(db.Model, SerializerMixin):
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(unique=True)
    passwordHash: Mapped[str]

    def set_password(self, password):
        self.passwordHash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.passwordHash, password)

def populate_db():
    products = [
        Product(id=1, description="Resistor 470 ohms", price=0.05),
        Product(id=2, description="Arduino Nano R3", price=50.00),
        Product(id=3, description="Raspberry PI 3", price=200.00),
    ]

    db.session.add_all(products)
  
    if not User.query.filter_by(username="admin").first():
        admin = User(username="admin")
        admin.set_password("admin123")  
        db.session.add(admin)

    db.session.commit()
  
