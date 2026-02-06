from flask import Blueprint, jsonify

checkout_bp = Blueprint('checkout', __name__)

@checkout_bp.route('/app/checkout_engine/<int:score>')
def checkout(score):
    # TEMP real logic placeholder
    if score > 170 or score < 2:
        return jsonify({"checkout": None})

    return jsonify({
        "score": score,
        "checkout": f"D{score // 2}" if score % 2 == 0 else "No out"
    })