from flask_restx import Api
from werkzeug.middleware.proxy_fix import ProxyFix

api = Api(version='1.0', title='API IPCA',
          description='API IPCA')


def init_app(app):
    app.wsgi_app = ProxyFix(app.wsgi_app)
    api.init_app(app)