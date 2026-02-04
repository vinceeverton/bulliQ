def double_percentage(throws):
    doubles = [t for t in throws if t.target.startswith("D")]
    hits = [t for t in doubles if t.hit]
    return len(hits) / max(len(doubles), 1)