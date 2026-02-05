import cv2
import psutil
import time
from flask import Flask, Response, render_template_string

app = Flask(__name__)

# ------------------------- Camera Setup -------------------------
def get_camera():
    camera = cv2.VideoCapture(0) 
    time.sleep(3)  # Allow camera to initialize
    return camera

camera = get_camera()

def camera_stream(): 
    while True:
        success, frame = camera.read()
        if not success:
            print("Camera frame not ready") 
            time.sleep(0.1)
            continue
            
        ret, buffer = cv2.imencode(".jpg", frame)
        if not ret:
            print("Encoding failed")
            continue 
            
        frame_bytes = buffer.tobytes() 
        # Correctly formatted multipart response
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

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
    <head><title>BulliQ Dashboard</title></head>
    <body>
        <h1>BulliQ Pi Dashboard</h1> 
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

@app.route("/health")
def health_route(): 
    health = get_health()
    return f"CPU: {health['cpu']}% | RAM: {health['ram']}% | Temp: {health['temp']} °C"

# ------------------------- Run Flask -------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7000, debug=True, use_reloader=False)
