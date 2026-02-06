import cv2
import time
import numpy as np
from flask import Blueprint, Response

camera_bp = Blueprint('camera', __name__)

camera = None  # global camera object

def get_camera():
    """Try to open camera 5 times"""
    global camera
    attempts = 0
    while attempts < 5:
        cam = cv2.VideoCapture(0)  # use /dev/video0
        if cam.isOpened():
            print("Camera opened successfully")
            return cam
        print(f"Camera not ready, attempt {attempts+1}/5")
        attempts += 1
        time.sleep(1)
    print("Camera could not be opened, using blank feed")
    return None

def camera_stream():
    global camera
    if camera is None:
        camera = get_camera()

    while True:
        if camera is None:
            # Blank frame if camera fails
            blank_frame = 255 * np.ones((480, 640, 3), dtype=np.uint8)
            ret, buffer = cv2.imencode('.jpg', blank_frame)
            frame_bytes = buffer.tobytes()
        else:
            success, frame = camera.read()
            if not success:
                # Camera not ready, wait and yield blank
                blank_frame = 255 * np.ones((480, 640, 3), dtype=np.uint8)
                ret, buffer = cv2.imencode('.jpg', blank_frame)
                frame_bytes = buffer.tobytes()
            else:
                # Flip the frame
                frame = cv2.flip(frame, -1)
                ret, buffer = cv2.imencode('.jpg', frame)
                frame_bytes = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

@camera_bp.route('/video_feed')
def video_feed():
    return Response(camera_stream(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')