# The binary_search function can now be used to solve other problems too. It is a tested piece of logic.
def binary_search(lo, hi, condition):
    while lo <= hi:
        mid = (lo + hi) // 2
        result = condition(mid)
        if result == "found":
            return mid
        elif result == "left":
            hi = mid - 1
        else:
        # result == "right"
            lo = mid + 1
    return -1

# Note here that we have defined a function within a function, another handy feature in Python. And the inner function can access the variables within the outer function.
def locate_card(cards, query):
    def condition(mid):
        if cards[mid] == query:
            if mid > 0 and cards[mid-1] == query:
                return "left"
            else:
                return "found"
        elif cards[mid] < query:
            return "left"
        else:
        # cards[mid] > query
            return "right"
    return binary_search(0, len(cards) - 1, condition)

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