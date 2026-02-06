from flask import Blueprint, jsonify

api_bp = Blueprint('api', __name__)

@api_bp.route('/api/checkout/<int:score>')
def checkout(score):
    return jsonify({
        "score": score,
        "checkout": "Not implemented yet"
    })