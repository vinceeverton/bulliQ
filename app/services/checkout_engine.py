from fastapi import APIRouter

# This creates the router that main.py will use
router = APIRouter(prefix="/api")

def get_dart_logic(score: int):
    """The actual math logic moved here"""
    if score > 170 or score < 2:
        return {"score": score, "checkout": None, "message": "No finish possible"}

    # Your logic: If even, suggest a Double. If odd, no standard out.
    if score % 2 == 0:
        return {
            "score": score, 
            "checkout": [f"D{score // 2}"],
            "message": "Finish found"
        }
    
    return {
        "score": score, 
        "checkout": None, 
        "message": "No standard out"
    }

@router.get("/checkout/{score}")
async def checkout_api(score: int):
    # This endpoint calls the logic function above
    return get_dart_logic(score)