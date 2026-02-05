import cv2
import time

camera = None

def get_camera():
    global camera
    if camera is not None:
        return camera

    attempts = 5
    for i in range(attempts):
        # Force V4L2 backend
        camera = cv2.VideoCapture(0, cv2.CAP_V4L2)
        if camera.isOpened():
            print(f"Camera opened on attempt {i+1}")
            return camera
        print(f"Camera attempt {i+1} failed, retrying...")
        camera.release()
        camera = None
        time.sleep(1)
    raise RuntimeError("Camera could not be opened after 5 attempts")

def camera_stream():
    cam = get_camera()
    while True:
        success, frame = cam.read()
        if not success:
            time.sleep(0.1)
            continue

        # Flip horizontally and vertically
        frame = cv2.flip(frame, -1)

        ret, buffer = cv2.imencode(".jpg", frame)
        if not ret:
            continue
        frame_bytes = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')