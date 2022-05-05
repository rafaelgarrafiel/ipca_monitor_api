from flask import Flask
from app.plugins import config


def create_app():
    """Factory to create a Flask app based on factory pattern"""
    app = Flask(__name__)
    config.init_app(app)
    return app