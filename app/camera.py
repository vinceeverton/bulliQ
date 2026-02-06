iimport cv2
import time
import numpy as np
from flask import Blueprint, Response

camera_bp = Blueprint('camera', __name__)

camera = None  # global camera

def get_camera():
    global camera  # <-- make sure we update the global camera
    attempts = 0
    while attempts < 5:
        camera = cv2.VideoCapture(0)
        if camera.isOpened():
            print("Camera opened successfully")
            return camera
        attempts += 1
        print(f"Camera not ready, attempt {attempts}/5")
        time.sleep(1)
    return None

def camera_stream():
    global camera
    if camera is None:
        camera = get_camera()
    if camera is None:
        # return blank frame if camera cannot be opened
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
                print("Camera frame not ready")
                time.sleep(0.1)
                continue
            frame = cv2.flip(frame, -1)  # flips horizontally and vertically
            ret, buffer = cv2.imencode(".jpg", frame)
            if not ret:
                continue
            frame_bytes = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

@camera_bp.route('/video_feed')
def video_feed():
    return Response(camera_stream(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')