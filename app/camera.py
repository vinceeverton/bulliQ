import cv2
from flask import Blueprint, Response
from .calibration import calibration
from .dart import detect_hit

camera_bp = Blueprint('camera', __name__)
cap = cv2.VideoCapture(0)

last_gray = None
hit_point = None
freeze_until = 0

def encode_frame(frame):
    ret, jpeg = cv2.imencode('.jpg', frame)
    return jpeg.tobytes() if ret else None

def process_frame(frame):
    global last_gray, hit_point, freeze_until

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)

    if last_gray is None:
        last_gray = gray
        return frame

    hit_point = detect_hit(gray, last_gray, calibration)
    last_gray = gray

    #draw hit point
    if hit_point:
        cv2.circle(frame, hit_point, 20, (0, 0, 255), -1)

    #draw calibration circles
    if calibration["center"]:
        cx, cy = calibration["center"]
        cv2.circle(frame, (cx, cy), 5, (0, 255, 0), -1)

    return frame
def gen_frames():
    while True:
        ret, frame = cap.read()
        if not ret:
            continue
        frame = process_frame(frame)
        frame_bytes = encode_frame(frame)
        if frame_bytes:
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')
            

@camera_bp.route('/video_feed')
def video_feed():
    return Response(gen_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')   

#def get_camera():
    camera = cv2.VideoCapture(0)
    time.sleep(3)  # allow camera to initialize
    return camera

#def camera_stream(camera):
    while True:
        success, frame = camera.read()
        if not success:
            time.sleep(0.1)
            continue

        ret, buffer = cv2.imencode(".jpg", frame)
        if not ret:
            continue

        frame = buffer.tobytes()
        yield (b"--frame\r\n"
               b"Content-Type: image/jpeg\r\n\r\n" + frame + b"\r\n")
