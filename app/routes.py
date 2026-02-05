from fastapi import APIRouter
from services.checkout_engine import best_checkout
from services.stats_engine import get_double_stats

router = APIRouter(prefix="/api")

@router.get("/checkout/{remaining}")
def checkout(remaining: int):
    stats = get_double_stats()
    route = best_checkout(remaining, stats)
    return {
        "remaining": remaining,
        "route": route
    }