import cv2
import time

def get_camera():
    attempts = 0
    while attempts < 5:
        camera = cv2.VideoCapture(0, cv2.CAP_V4L2)  # Avoid GStreamer
        if camera.isOpened():
            return camera
        attempts += 1
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

        # Flip camera horizontally and vertically
        frame = cv2.flip(frame, -1)

        ret, buffer = cv2.imencode(".jpg", frame)
        if not ret:
            continue

        frame_bytes = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')