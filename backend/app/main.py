from fastapi import FastAPI
from routes import router

app = FastAPI(title="BullIQ API")
app.include_router(router)
