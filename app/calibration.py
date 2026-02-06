from flask import Blueprint, jsonify

calib_bp = Blueprint('calibration', __name__)

@calib_bp.route('/calibrate', methods=['POST'])
def calibrate():
    print("Calibration hit")
    return jsonify({"status": "ok"})