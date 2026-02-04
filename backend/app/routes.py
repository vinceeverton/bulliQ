from fastapi import APIRouter
from app.services.checkout_engine import best_checkout

router = APIRouter()

@router.get("/checkout/{remaining}")
def checkout(remaining: int):
    fake_stats = {"D16": 0.65, "D20": 0.45}
    return {"route": best_checkout(remaining, fake_stats)}