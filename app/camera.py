import cv2
import time
from flask import Response

def get_camera():
    for i in range(5):
        camera = cv2.VideoCapture(0)  # or 1 if needed
        if camera.isOpened():
            return camera
        camera.release()
        time.sleep(1)
    raise RuntimeError("Camera could not be opened after 5 attempts")

camera = get_camera()

def camera_stream():
    while True:
        success, frame = camera.read()
        if not success:
            print("Camera frame not ready")
            time.sleep(0.1)
            continue

        frame = cv2.flip(frame, -1)  # flip horizontally and vertically

        ret, buffer = cv2.imencode(".jpg", frame)
        if not ret:
            print("Encoding failed")
            continue

        frame_bytes = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')