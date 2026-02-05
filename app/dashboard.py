from flask import flask Blueprint
import psutil

dashboard_bp = Blueprint("dashboard", __name__)

@dashboard_bp.route("/dashboard")
def stats():
    return {
         "cpu": psutil.cpu_percent(),
         "ram": psutil.virtual_memory().percent
    }
