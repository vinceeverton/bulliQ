def punishment_task(remaining: int):
    if remaining <= 40 and remaining % 2 == 0:
        return f"Hit {remaining // 2} doubles in a row"

    if remaining > 60:
        return "Score 100+ before returning"

    return "Throw until bust, then reset"