from typing import List


def average_rating(rating_list: List) -> int:
    """Calculates the average rating of a book from the list."""
    if not rating_list:
        return 0
    return round(sum(rating_list) / len(rating_list))
