def punishment(miss):
    punish = {
        "D20": "D10",
        "D16": "D8",
        "D10": "D5"
    }
    return punish.get(miss, "D1")
