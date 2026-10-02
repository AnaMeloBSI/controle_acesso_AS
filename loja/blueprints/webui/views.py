from loja.ext.database import db
from loja.model import Product, User
from flask import render_template, request, redirect, url_for, session

def index():
    products = db.session.execute(
        db.select(Product).order_by(Product.description)).scalars()

    return render_template("products.html", products=products)

def product(product_id):
    if 'usuario_logado' not in session:
        return redirect(url_for('webui.login'))

    product = db.session.execute(
        db.select(Product).filter_by(id=product_id)).scalar()

    return render_template("product.html", product=product)

def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = db.session.execute(
            db.select(User).filter_by(username=username)).scalar()

        if user and user.check_password(password):
            session['usuario_logado'] = user.id
            return redirect(url_for('webui.index'))

        return render_template("login.html", error="Usuário ou senha inválidos!")

    return render_template("login.html")

def logout():
    session.pop('usuario_logado', None)
    return redirect(url_for('webui.login'))