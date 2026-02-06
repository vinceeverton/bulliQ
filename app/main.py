import uvicorn
import psutil
import os
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

# Note the absolute imports
from app.services.api import router as api_router
from app.services.camera import router as camera_router
from app.services.calibration import calib_bp as calib_router
# from app.services.routes import router as routes_router 

app = FastAPI()

# Pathing: Since main.py is in /app, static is in ./static
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
app.mount("/static", StaticFiles(directory=os.path.join(CURRENT_DIR, "static")), name="static")
templates = Jinja2Templates(directory=os.path.join(CURRENT_DIR, "templates"))

# Include Routers
app.include_router(api_router)
app.include_router(camera_router)
app.include_router(calib_router)

@app.get("/")
async def index(request: Request):
    temp = "N/A"
    try:
        with open("/sys/class/thermal/thermal_zone0/temp", "r") as f:
            temp = round(int(f.read()) / 1000, 1)
    except: pass

    health = {
        "cpu": psutil.cpu_percent(),
        "ram": psutil.virtual_memory().percent,
        "temp": temp
    }
    return templates.TemplateResponse("index.html", {"request": request, **health})

