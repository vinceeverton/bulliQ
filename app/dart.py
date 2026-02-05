import numpy as np
from math import hypot, atan2, degrees

BOARD = [20, 1, 18, 4, 13, 6, 10, 15, 2, 17, 3, 19, 7, 16, 8, 11, 14, 9, 12, 5]

def detect_hit(gray, last_gray, calib):
    frame_delta = cv2.absdiff(last_gray, gray)
    thresh = cv2.threshold(frame_delta, calib['motion_threshold'], 255, cv2.THRESH_BINARY)[1]
    thresh = cv2.dilate(thresh, None, iterations=2)
    cnts, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for c in cnts:
        if cv2.contourArea(c) < 500:
            continue

        x, y, w, h = cv2.boundingRect(c)
        return (x+w//2, y+h//2)
    return None
def compute_score(x, y, calib):
        if not calib["center"]:
            return 0
         cx, cy = calib["center"]
        r = hypot(x - cx, y - cy)
        angle = (degrees(atan2(cy - y, x - cx)) + 360 + 90) %360
        segment = BOARD[int(angle // 18)]
        if r < calib["bull"]:
            return 50 
        elif r < calib["outer_bull"]:
            return 25  
        elif r > calib["triple_inner"] and r < calib["triple_outer"]:
            return segment * 3
        elif r > calib["double_inner"] and r < calib["double_outer"]:
            return segment * 2
        else:
            return segment 