import cv2
import json
import psutil
import time
import numpy as np
from math import atan2, degrees, hypot
from flask import Flask, Response, render_template, Response, request

app = Flask(__name__)

# ------------------------- Camera Setup -------------------------
def camera_stream():
    last_gray = None
    hit_point = None
    freeze_until = 0

    while True:
        success, frame = camera.read()
        if not success:
            print("Camera frame not ready") 
            time.sleep(0.1)
            continue

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (21, 21), 0)

        if last_gray is None:
            last_gray = gray
        else:
            frame_delta = cv2.absdiff(last_gray, gray)
            thresh = cv2.threshold(frame_delta, 25, 255, cv2.THRESH_BINARY)[1]
            thresh = cv2.dilate(thresh, None, iterations=2)
            cnts, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            for c in cnts:
                if cv2.contourArea(c) < 500:
                    continue
                x, y, w, h = cv2.boundingRect(c)
                hit_point = (x + w//2, y + h//2)
                freeze_until = time.time() + 1.0

        last_gray = gray

        # Draw hit point
        if hit_point:
            cv2.circle(frame, hit_point, 10, (0, 0, 255), -1)

        ret, buffer = cv2.imencode(".jpg", frame)
        if ret:
            frame_bytes = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')


BOARD = [20,1,18,4,13,6,10,15,2,17,3,19,7,16,8,11,14,9,12,5]
# -------------------------  score calculation -------------------------

def score_dart(x, y, calib):
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

calibration = {
    "center": None,
    "bull": 12,
    "outer_bull": 25,
    "triple_inner": 120,
    "triple_outer": 140,
    "double_inner": 190,
    "double_outer": 210
}

def save_calibration():
    with open("calibration.json", "w") as f:
        json.dump(calibration, f)
try:
    with open("calibration.json") as f:
        calibration.update(json.load(f))
except:
    pass


# ------------------------- Health function -------------------------
def get_health():
    cpu = psutil.cpu_percent(interval=1) 
    ram = psutil.virtual_memory().percent
    try:
        # Standard path for Raspberry Pi temperature
        with open("/sys/class/thermal/thermal_zone0/temp") as f:
            temp = int(f.read()) / 1000 
    except Exception:
        temp = "N/A"
    return {"cpu": cpu, "ram": ram, "temp": temp}

# ------------------------- Routes -------------------------
@app.route("/")
def index():
    health = get_health()
    html = """
    <html> 
    <head><title>BulliQ</title></head>
    <body>
        <h1>BulliQ</h1> 
        <h2>System Health</h2>
        <ul>
            <li>CPU Usage: {{ cpu }}%</li> 
            <li>RAM Usage: {{ ram }}%</li> 
            <li>Temp: {{ temp }} °C</li>
        </ul>
        <h2>Camera Feed</h2>
        <img src="/camera_feed" width="640" height="480"/>
    </body>
    </html>
    """
    return render_template_string(html, cpu=health['cpu'], ram=health['ram'], temp=health['temp'])

@app.route("/camera_feed")
def camera_feed(): 
    return Response(camera_stream(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route("/calibrate", methods=["POST"])
def calibrate():
    data = request.json
    calibration["center"] = (data["x"], data["y"])
    save_calibration()
    return {"status": "saved"}

@app.route("/health")
def health_route(): 
    health = get_health()
    return f"CPU: {health['cpu']}% | RAM: {health['ram']}% | Temp: {health['temp']} °C"

# ------------------------- Run Flask -------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7000, debug=True, use_reloader=False)
