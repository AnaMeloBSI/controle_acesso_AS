
import os

from dotenv import load_dotenv
from flask import (
    render_template,
    request,
    redirect,
    url_for,
    session,
    flash
)
from werkzeug.security import check_password_hash

from loja.ext.database import db
from loja.model import Product


# Carrega as configurações do arquivo .env
load_dotenv(override=True)


def index():
    products = db.session.execute(
        db.select(Product).order_by(Product.description)
    ).scalars()

    return render_template(
        "products.html",
        products=products
    )


def product(product_id):
    product = db.session.execute(
        db.select(Product).filter_by(id=product_id)
    ).scalar()

    return render_template(
        "product.html",
        product=product
    )


def login():
    if request.method == "POST":

        # Dados digitados no formulário
        usuario = request.form.get("usuario", "").strip()
        senha = request.form.get("senha", "")

        # Credenciais configuradas no arquivo .env
        usuario_admin = os.getenv("ADMIN_USERNAME", "").strip()
        senha_hash = os.getenv("ADMIN_PASSWORD_HASH", "").strip()

        # Verifica se as credenciais estão configuradas
        if not usuario_admin or not senha_hash:
            flash(
                "Configuração do administrador não encontrada.",
                "error"
            )
            return render_template("login.html")

        # Verifica o usuário e a senha
        try:
            senha_correta = check_password_hash(
                senha_hash,
                senha
            )
        except (ValueError, TypeError):
            senha_correta = False

        if usuario == usuario_admin and senha_correta:

            session.clear()
            session["admin_logado"] = True

            flash(
                "Login realizado com sucesso!",
                "success"
            )

            return redirect(url_for("admin.index"))

        flash(
            "Usuário ou senha incorretos.",
            "error"
        )

    return render_template("login.html")


def logout():
    session.clear()

    flash(
        "Você saiu da área administrativa.",
        "success"
    )

    return redirect(url_for("webui.login"))
