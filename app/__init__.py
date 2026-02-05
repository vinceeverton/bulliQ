from flask import Flask

def create_app():
    app = Flask(__name__)

    from .routes import main
    from .camera import camera_bp
    from .calibration import calib_bp
    from .dashboard import dashboard_bp

    app.register_blueprint(main)
    app.register_blueprint(camera_bp, url_prefix="/camera")
    app.register_blueprint(calib_bp, url_prefix="/calibration")
    app.register_blueprint(dashboard_bp, url_prefix="/dashboard")

    return app
