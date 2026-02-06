# BulliQ Dart Tracker 🎯

An asynchronous dart tracking and checkout system built with **FastAPI** and **OpenCV**, optimized for the Raspberry Pi.

## 📁 Project Structure

BulliQ/
├── run.py               # Application launcher
├── README.md            # Setup instructions
├── requirements.txt      # Dependencies
└── app/
    ├── main.py          # FastAPI application & routing logic
    ├── services/        # Logic modules (Camera, API, Calibration)
    ├── static/          # CSS and JavaScript
    └── templates/       # HTML Dashboard
🛠️ Installation

git clone 
cd bulliQ

Setup Virtual Environment (Recommended for Pi)
python -m venv venv
source venv/bin/activate

 Install Dependencies
 pip install fastapi uvicorn psutil jinja2 numpy opencv-python-headless

 🚀 Running the App
Start the server using the terminal:

python run.py

The dashboard will be available at: http://<your-pi-ip>:7000

⚙️ Features
Asynchronous Video Streaming: High-performance camera feed using FastAPI's StreamingResponse.
Intelligent Checkout API: Instant checkout suggestions based on your remaining score.
System Health Monitor: Real-time tracking of Pi CPU, RAM, and Temperature.
Calibration System: Save and load camera calibration settings via JSON.

📝 Troubleshooting
Camera Busy: Ensure no other process (like a legacy Flask app) is using /dev/video0. Use sudo fuser -k /dev/video0 to clear it.
Static Files 404: Ensure app/main.py correctly mounts the static directory using absolute paths.


