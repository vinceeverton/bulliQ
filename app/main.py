import uvicorn
import psutil
import os
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles  # Fixed import
from fastapi.templating import Jinja2Templates

# Absolute imports from your services
from app.services.api import router as api_router
from app.services.camera import router as camera_router
from app.services.calibration import router as calib_router

app = FastAPI()

# Get the absolute path to the 'app' directory
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

# Mount Static and Templates correctly
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
    except: 
        pass

    health = {
        "cpu": psutil.cpu_percent(),
        "ram": psutil.virtual_memory().percent,
        "temp": temp
    }
    return templates.TemplateResponse("index.html", {"request": request, **health})

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=7000)
