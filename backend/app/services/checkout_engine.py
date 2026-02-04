import json

with open("app/data/checkout_table.json") as f:
    CHECKOUTS = json.load(f)

def best_checkout(remaining, double_stats):
    routes = CHECKOUTS.get(str(remaining), [])
    ranked = []

    for route in routes:
        prob = 1.0
        for dart in route:
            if dart.startswith("D"):
                prob *= double_stats.get(dart, 0.3)
            else:
                prob *= 0.85
        ranked.append((route, prob))

    ranked.sort(key=lambda x: x[1], reverse=True)
    return ranked[0][0] if ranked else []
