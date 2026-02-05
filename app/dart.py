from math import atan2, degrees, hypot

# Dartboard numbering, clockwise starting at top
BOARD = [20, 1, 18, 4, 13, 6, 10, 15, 2, 17,
         3, 19, 7, 16, 8, 11, 14, 9, 12, 5]

def detect_hit(x, y, calib):
    """
    Calculate dart score based on hit coordinates and calibration data
    """
    if calib.get("center") is None:
        return None

    cx, cy = calib["center"]

    r = hypot(x - cx, y - cy)
    angle = (degrees(atan2(cy - y, x - cx)) + 360 + 90) % 360
    segment = BOARD[int(angle // 18)]

    if r < calib["bull"]:
        return 50
    elif r < calib["outer_bull"]:
        return 25
    elif calib["triple_inner"] < r < calib["triple_outer"]:
        return segment * 3
    elif calib["double_inner"] < r < calib["double_outer"]:
        return segment * 2
    else:
        return segment