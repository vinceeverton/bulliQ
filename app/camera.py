# /home/shadow/bulliQ/app/camera.py
import cv2
import time

def get_camera():
    camera = cv2.VideoCapture(0)
    time.sleep(3)  # allow camera to initialize
    return camera

def camera_stream(camera):
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
