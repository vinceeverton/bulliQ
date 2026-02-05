import cv2
import time

# ------------------------- Camera Setup -------------------------
def get_camera():
    attempts = 0
    while attempts < 5:
        camera = cv2.VideoCapture(0)  # USB camera or /dev/video0
        if camera.isOpened():
            print("Camera opened successfully")
            return camera
        print(f"Camera not ready, attempt {attempts+1}/5")
        attempts += 1
        time.sleep(1)
    return None  # Fail gracefully

camera = None  # Do not open on import

def camera_stream():
    global camera
    if camera is None:
        camera = get_camera()
        if camera is None:
            # Return a blank frame if camera can't be opened
            import numpy as np
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
            ret, buffer = cv2.imencode(".jpg", frame)
            if not ret:
                print("Encoding failed")
                continue
            frame_bytes = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')