from flask import Flask
from app import create_app
app = create_app()
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7000, debug=True)
    
def create_app():
    # explicitly set template folder
    app = Flask(__name__, template_folder="../templates")

    from .routes import main_bp
    app.register_blueprint(main_bp)

    return app