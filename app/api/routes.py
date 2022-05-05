from app.api.ipca.api import api as ipca_api
from app.plugins.api import api


def init_app(app):
    api.add_namespace(ipca_api)

