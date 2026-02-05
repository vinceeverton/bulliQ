from flask import Blueprint, Response
from app.camera import camera_stream

main = Blueprint('main', __name__)

@main.route('/video_feed')
def video_feed():
    return Response(camera_stream(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')