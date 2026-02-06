import cv2
import numpy as np
from fastapi import APIRouter
from fastapi.responses import StreamingResponse

router = APIRouter()
camera = cv2.VideoCapture(0)

def generate_frames():
    while True:
        success, frame = camera.read()
        if not success:
            break
        
        # Performance trick: Flip and resize here if needed for Pi speed
        frame = cv2.flip(frame, -1)
        _, buffer = cv2.imencode('.jpg', frame)
        
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + buffer.tobytes() + b'\r\n')

@router.get("/video_feed")
async def video_feed():
    return StreamingResponse(generate_frames(), 
                             media_type="multipart/x-mixed-replace;boundary=frame")

