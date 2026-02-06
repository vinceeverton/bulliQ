import uvicorn
import psutil
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from .services import camera, api

app = FastAPI()

# Mount Static and Templates
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Include Service Routers
app.include_router(camera.router)
app.include_router(api.router)

@app.get("/")
async def index(request: Request):
    # System Health logic for your Pi dashboard
    health = {
        "cpu": psutil.cpu_percent(),
        "ram": psutil.virtual_memory().percent,
        "temp": 0 # You can add Pi temp logic here
    }
    return templates.TemplateResponse("index.html", {"request": request, **health})

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=7000)
