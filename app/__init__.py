from flask import Flask

def create_app():
    app = Flask(__name__, template_folder="../templates", static_folder="../static")

    # Import and register all blueprints
    from .routes import routes_bp
    from .camera import camera_bp
    from .calibration import calib_bp
    from .dashboard import dashboard_bp

    app.register_blueprint(routes_bp)
    app.register_blueprint(camera_bp, url_prefix='/camera')
    app.register_blueprint(calib_bp, url_prefix='/calibration')
    app.register_blueprint(dashboard_bp, url_prefix='/dashboard')

    from .  import routes 

    return app