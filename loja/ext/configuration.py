
import os

from dotenv import load_dotenv
from dynaconf import FlaskDynaconf


def init_app(app, **config):
    load_dotenv()

    FlaskDynaconf(app, **config)

    secret_key = os.getenv("SECRET_KEY")

    if not secret_key:
        raise RuntimeError(
            "Configure SECRET_KEY no arquivo .env antes de iniciar."
        )

    app.config["SECRET_KEY"] = secret_key
    app.config["SESSION_COOKIE_HTTPONLY"] = True
    app.config["SESSION_COOKIE_SAMESITE"] = "Lax"
