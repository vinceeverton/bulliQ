import sys
print(sys.path)
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from routes import router

app = FastAPI(title="BullIQ")

# Serve static files (CSS / JS)
app.mount("/static", StaticFiles(directory="static"), name="static")

# HTML templates
templates = Jinja2Templates(directory="templates")

@app.get("/")
def ui(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# API routes
app.include_router(router)