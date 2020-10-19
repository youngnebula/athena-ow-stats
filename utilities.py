from jsondiff import diff
# from typing import Dict, TypedDict


def get_rank(rating: int) -> str:
    """Returns the rating as a text rank

    Args:
        rating (int): integer rank of Player

    Returns:
        str: string rank of Player
    """
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


def difference_data(new_data, old_data):
    """Finds the difference between two dictionaries

    Args:
        new_data (Dict[]): Newer (larger) dictionary containing updated stats
        old_data (Dict[]): Older (smaller) dictionary

    Returns:
        Dict: A new dictionary containing only the difference stats
    """
    post_diff = diff(new_data, old_data)
    pre_diff = diff(old_data, new_data)
    return find_diffs(post_diff, pre_diff)


def find_diffs(d1, d2):
    """Trims off any duplicated or non-updated values from two dictionaries.

    Args:
        d1 ([type]): [description]
        d2 ([type]): [description]

    Returns:
        [type]: [description]
    """
    if isinstance(d1, dict) and isinstance(d2, dict):
        return {k: find_diffs(d1.get(k, 0),
                d2.get(k, 0)) for k in d1 if k in d2}
    else:
        return d1 - d2
