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


### How the Code Works (Function Closure) ###
### The Example Scenario ###
# Imagine you call the function like this:

# locate_card([10, 6, 6, 3], 6)
# cards = [10, 6, 6, 3] (sorted in descending order)
# query = 6 (the target we want the first index of)

# Step-by-Step Execution Trace
# Step 1: Initializing locate_card
# When you hit locate_card([10, 6, 6, 3], 6):

# Python enters locate_card and creates a local sandbox for it containing cards and query.
# Python sees def condition(mid):. It does not run the code inside condition yet. It just reads it, packages it up, and remembers it.
# Because condition was created inside locate_card, it gets a superpower called a closure: it memorizes the current values of cards ([10, 6, 6, 3]) and query (6).
# Wherever condition goes, it carries this memory with it.

# Step 2: Handing off to binary_search
# Python reaches the last line of locate_card:

# return binary_search(0, 3, condition)
# 0 becomes lo
# 3 (which is 4 - 1) becomes hi
# The condition function itself is passed in as the third argument.

# Now, control jumps up to the binary_search function.

# Step 3: Inside the binary_search loop
# Loop Round 1:
# Calculate mid: mid = (0 + 3) // 2 which is 1.

# The Call: result = condition(1)
# Control jumps back to the condition function. Remember, condition still knows cards and query!

# Inside condition(1): Is cards[1] == query? cards[1] is 6, and query is 6. Yes!
# It checks duplicates: if 1 > 0 and cards[0] == 6: -> cards[0] is 10. 10 == 6 is False.
#It goes to the inner else and returns 'found'.

# Back in binary_search:
# result is now 'found'.
# The if result == 'found': block triggers, and it immediately executes return mid (which is 1).

# A More Interesting Trace (Triggers the Closure Logic)
# What if we call it with a slightly larger list where it takes more than one step?

# locate_card([10, 8, 6, 6, 3], 6)  # cards length is 5
# Loop Round 1:
# lo = 0, hi = 4
# mid = (0 + 4) // 2 -> 2

# result = condition(2)
# Inside condition(2): cards[2] is 6. Match!

#Check duplicates: if 2 > 0 and cards[1] == 6: -> cards[1] is 8. 8 == 6 is False.
# Returns 'found'.
# binary_search receives 'found', returns mid (2). Done.

# What if the mid was index 3? (Let's simulate if the math landed us at index 3):
# mid = 3
# result = condition(3)

# Inside condition(3): cards[3] is 6. Match!
# Check duplicates: if 3 > 0 and cards[2] == 6: -> cards[2] is 6. 6 == 6 is True!
# Returns 'left'.

# Back in binary_search, result is 'left'.

# It hits the elif result == 'left': block and updates hi = mid - 1 (3 - 1 = 2).

# The loop continues with a narrower search window!

# Summary of the Mechanism
# Think of it like a manager (locate_card) hiring a contractor (binary_search) to do a job.
# The manager writes down specific rules for checking a card on a sticky note (condition) and hands that sticky note to the contractor.
# The contractor moves the lo and hi boundaries around blindly, and every time they pick a middle index, they look at the manager's sticky note to ask,
# "What should I do with this index?" The sticky note responds with 'left', 'right', or 'found', and the contractor adjusts accordingly.