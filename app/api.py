from flask import Blueprint, jsonify
api_bp = Blueprint('api', __name__)

# Simple, real checkout table (will expand later)
CHECKOUTS = {
    170: ["T20", "T20", "Bull"],
    167: ["T20", "T19", "Bull"],
    164: ["T20", "T18", "Bull"],
    161: ["T20", "T17", "Bull"],
    160: ["T20", "T20", "D20"],
    158: ["T20", "T20", "D19"],
    157: ["T20", "T19", "D20"],
    156: ["T20", "T20", "D18"],
    155: ["T20", "T19", "D19"],
    154: ["T20", "T18", "D20"],
    153: ["T20", "T19", "D18"],
    152: ["T20", "T20", "D16"],
    151: ["T20", "T17", "D20"],
    150: ["T20", "T18", "D18"],
    149: ["T20", "T19", "D16"],
    148: ["T20", "T16", "D20"],
    147: ["T20", "T17", "D18"],
    146: ["T20", "T18", "D16"],
    145: ["T20", "T15", "D20"],
    144: ["T20", "T20", "D12"],
    141: ["T20", "T19", "D12"],
    140: ["T20", "T20", "D10"],
    121: ["T20", "11", "Bull"],
    120: ["T20", "20", "D20"],
    100: ["T20", "D20"],
    80: ["T20", "D10"],
    60: ["20", "D20"],
    50: ["Bull"],
    40: ["D20"],
    32: ["D16"],
    24: ["D12"],
    20: ["D10"],
    16: ["D8"],
    8: ["D4"],
    2: ["D1"],
}

@api_bp.route("/checkout/<int:score>")
def checkout(score):
    if score < 2:
        return jsonify({
            "score": score,
            "checkout": None,
            "message": "Finish not possible"
        })

    if score in CHECKOUTS:
        return jsonify({
            "score": score,
            "checkout": CHECKOUTS[score],
            "darts": len(CHECKOUTS[score])
        })

    if score > 170:
        return jsonify({
            "score": score,
            "checkout": None,
            "message": "Score too high to finish"
        })

    return jsonify({
        "score": score,
        "checkout": None,
        "message": "No standard checkout"
    })