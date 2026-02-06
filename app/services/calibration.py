# app/services/calibration.py
from fastapi import APIRouter, Request, HTTPException
import json
import os

# Change Blueprint to APIRouter
router = APIRouter() 
CALIB_FILE = "calibration.json"

@router.post('/calibrate')
async def calibrate(request: Request):
    try:
        data = await request.get_json() # FastAPI way to get JSON
    except:
        data = await request.json()

    if not data:
        raise HTTPException(status_code=400, detail="No data")

    with open(CALIB_FILE, "w") as f:
        json.dump(data, f)

    return {"status": "calibration saved"}
