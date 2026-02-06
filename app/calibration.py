from flask import Blueprint, request, jsonify
import json
import os

calib_bp = Blueprint('calibration', __name__)

CALIB_FILE = "calibration.json"

@calib_bp.route('/calibration', methods=['POST'])
def calibrate():
    data = request.get_json()

    if not data:
        return jsonify({"error": "No data"}), 400

    with open(CALIB_FILE, "w") as f:
        json.dump(data, f)

    return jsonify({"status": "calibration saved"})