from flask import Flask
from flask import Blueprint, Response, render_template
from app.camera import camera_stream  # function from camera.py

main = Blueprint("main", __name__)

@main.route("/")
def index():
    return render_template("index.html")

@main.route("/camera_feed")
def camera_feed():
    return Response(camera_stream(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')