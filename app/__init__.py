from flask import Flask

def create_app():
    app = Flask(__name__)

    # Instead of blueprints, import routes directly
    from . import routes

    return app