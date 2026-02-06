from fastapi import APIRouter

router = APIRouter()

# The full checkout table
CHECKOUTS = {
    170: ["T20", "T20", "Bull"],
    167: ["T20", "T19", "Bull"],
    160: ["T20", "T20", "D20"],
    120: ["T20", "20", "D20"],
    100: ["T20", "D20"],
    60: ["20", "D20"],
    50: ["Bull"],
    40: ["D20"],
    32: ["D16"]
}

@router.get("/api/checkout/{score}")
async def checkout(score: int):
    if score in CHECKOUTS:
        return {
            "score": score,
            "checkout": CHECKOUTS[score] # Returns the list: ["T20", "T20", "Bull"]
        }
    
    # Fallback for even numbers not in the list
    if 2 <= score <= 40 and score % 2 == 0:
        return {"score": score, "checkout": [f"D{score // 2}"]}

    return {"score": score, "checkout": None, "message": "No standard checkout"}
