# dashbboard
import flask import Blueprint, jsonify

dashboard_bp = Blueprint("dashboard", __name__)

@dashboard_bp.route("/dashboard")
def dashboard():
    cpu = psutil.cpu_percent()
    ram = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    try:
        with open("/sys/class/thermal/thermal_zone0/temp") as f:
            temp = int(f.read()) / 1000
    except:
        temp = 0
        
    data = {
        "cpu": cpu,
        "ram": ram,
        "disk": disk,
        "temp": temp
    }
    return jsonify(data)