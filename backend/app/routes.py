from fastapi import APIRouter
from services.checkout_engine import best_checkout
from services.practice_engine import punishment_task
from services.stats_engine import get_double_stats

router = APIRouter()


@router.get("/checkout/{remaining}")
def checkout(remaining: int):
    stats = get_double_stats()
    route = best_checkout(remaining, stats)
    return {
        "remaining": remaining,
        "route": route
    }


@router.get("/practice/{remaining}")
def practice(remaining: int):
    return {
        "task": punishment_task(remaining)
    }