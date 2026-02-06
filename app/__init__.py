from flask import Flask
from .api import api_bp
from .checkout_engine import checkout_bp

def create_app():
    app = Flask(
        __name__,
        template_folder="../templates",
        static_folder="../static"
        )

    # Import and register all blueprints
    from .routes import routes_bp
    from .camera import camera_bp
    from .calibration import calib_bp
    #from .dashboard import dashboard_bp

    app.register_blueprint(routes_bp) 
    app.register_blueprint(camera_bp)
    app.register_blueprint(calib_bp)
    app.register_blueprint(api_bp)
    app.register_blueprint(checkout_bp)
    #app.register_blueprint(dashboard_bp)
    

    return app