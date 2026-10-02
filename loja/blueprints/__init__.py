from .webui import init_app as init_webui
from .restapi import init_app as init_restapi

def init_app(app):
    init_webui(app)
    init_restapi(app)