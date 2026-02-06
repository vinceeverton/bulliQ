import cv2
import time
import numpy as np
from flask import Blueprint, Response

camera_bp = Blueprint('camera', __name__)

camera = None

def get_camera():
    attempts = 0
    while attempts < 5:
        camera = cv2.VideoCapture(0)
        if camera.isOpened():
            print("Camera opened successfully")
            return camera
        attempts += 1
        time.sleep(1)
    return None

def camera_stream():
    global camera
    if camera is None:
        camera = get_camera()
    if camera is None:
        blank_frame = 255 * np.ones((480, 640, 3), dtype=np.uint8)
        while True:
            ret, buffer = cv2.imencode(".jpg", blank_frame)
            frame_bytes = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')
    else:
        while True:
            success, frame = camera.read()
            if not success:
                time.sleep(0.1)
                continue
            frame = cv2.flip(frame, -1)
            
            ret, buffer = cv2.imencode(".jpg", frame)
            frame_bytes = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

@camera_bp.route('/video_feed')
def video_feed():
    return Response(camera_stream(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')