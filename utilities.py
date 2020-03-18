def get_rank(rating):
    """Returns the rating as a text rank"""
    if rating < 1500:
        rank = "Bronze"
    elif rating in range(1500, 2000):
        rank = "Silver"
    elif rating in range(2000, 2500):
        rank = "Gold"
    elif rating in range(2500, 3000):
        rank = "Platinum"
    elif rating in range(3000, 3500):
        rank = "Diamond"
    elif rating in range(3500, 4000):
        rank = "Master"
    elif rating >= 4000:
        rank = "Grandmaster"
    return rank


def find_diffs(d1, d2):
    """Finds the difference(subtraction) between two dictionaries"""
    if isinstance(d1, dict) and isinstance(d2, dict):
        return {k: find_diffs(d1.get(k, 0), d2.get(k, 0)) for k in d1 if k in d2}
    else:
        return d1 - d2