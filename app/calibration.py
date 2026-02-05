import json
from flask import Blueprint, request

calib_bp = Blueprint('calibration', __name__)

calibration = {
    "center": None,
    "bull": 12,
    "outer_bull": 25,
    "triple_inner": 120,
    "triple_outer": 140,
    "double_inner": 190,
    "double_outer": 210

}

# load saved calibration
try:
    with open("calibration.json") as f:
        calibration.update(json.load(f))
except:
    pass

def save_calibration():
    with open("calibration.json", "w") as f:
        json.dump(calibration, f)

@calib_bp.route("/calibrate", methods=["POST"])
def calibrate():
    data = request.json
    calibration["center"] = (data["x"], data["y"])
    save_calibration()
    return {"status": "success"}