from fastapi import APIRouter

router = APIRouter(prefix="/api")

CHECKOUTS = {
    170: ["T20", "T20", "Bull"],
    120: ["T20", "20", "D20"],
    60: ["20", "D20"]
}

@router.get("/checkout/{score}")
async def get_checkout(score: int):
    if score in CHECKOUTS:
        return {"score": score, "checkout": CHECKOUTS[score]}
    return {"score": score, "checkout": None, "message": "No standard checkout"}
