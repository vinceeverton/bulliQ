from flask import Flask
from .api import api_bp
from .camera import camera_bp
# from .calibration import calib_bp  # Ensure this exists or keep commented

def create_app():
    app = Flask(__name__, template_folder="../templates", static_folder="../static")

    # Register blueprints
    app.register_blueprint(camera_bp)
    app.register_blueprint(api_bp, url_prefix='/api') # Matches fetch('/api/...')
    
    return app
