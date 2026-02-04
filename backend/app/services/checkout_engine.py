CHECKOUTS = {
    170: ["T20", "T20", "BULL"],
    167: ["T20", "T19", "BULL"],
    164: ["T20", "T18", "BULL"],
    161: ["T20", "T17", "BULL"],
    40: ["D20"],
    32: ["D16"],
    24: ["D12"],
    16: ["D8"],
    8: ["D4"],
    2: ["D1"],
}


def best_checkout(remaining: int, double_stats: dict):
    if remaining in CHECKOUTS:
        return CHECKOUTS[remaining]

    # fallback logic
    for d in sorted(double_stats, key=double_stats.get, reverse=True):
        value = int(d.replace("D", "")) * 2
        if remaining - value >= 0:
            return [d]

    return ["No checkout"]