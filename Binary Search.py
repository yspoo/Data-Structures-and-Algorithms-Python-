def locate_card(cards, query):
    """
    Locate the position of the query in the cards list.

    Args:
        cards (list): A list of integers representing the cards.
        query (int): The integer value to locate in the cards list.

    Returns:
        int: The index of the query in the cards list, or -1 if not found.
    """
    lo, hi = 0, len(cards) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        result = test_location(cards, query, mid)

        if result == "found":
            return mid
        elif result == "left":
            hi = mid - 1
        elif result == "right":
            lo = mid + 1
    return -1

def test_location(cards, query, mid):
    mid_number = cards[mid]
    if mid_number == query:
        if mid-1 >= 0 and cards[mid-1] == query:
            return "left"
        else:
            return "found"
    elif mid_number < query:
        return "left"
    else:
        return "right"


### Test cases ###
cards = [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0]
query = 6
print(locate_card(cards, query))  # Output: 2

cards = [9, 7, 5, 2, -9]
query = 4
print(locate_card(cards, query))  # Output: -1

cards = [3, -1, -9, -127]
query = -127
print(locate_card(cards, query))  # Output: 3