### Question: ###

# You are given list of numbers, obtained by rotating a sorted list an unknown number of times. 
# Write a function to determine the minimum number of times the original sorted list was rotated to obtain the given list. 
# Your function should have the worst-case complexity of O(log N), where N is the length of the list. You can assume that all the numbers in the list are unique.

# Example: The list [5, 6, 9, 0, 2, 3, 4] was obtained by rotating the sorted list [0, 2, 3, 4, 5, 6, 9] 3 times.

# We define "rotating a list" as removing the last element of the list and adding it before the first element. E.g. rotating the list [3, 2, 4, 1] produces [1, 3, 2, 4].

# "Sorted list" refers to a list where the elements are arranged in the increasing order e.g. [1, 3, 5, 7].

### End of Question ###

def rotation_count_binary(arr):
    """
    This function takes a rotated sorted array as input and returns the number of times the original sorted array was rotated.
    It uses a binary search approach to find the index of the minimum element, which corresponds to the number of rotations.
    
    :param arr: List[int] - A list of unique integers that has been rotated.
    :return: int - The number of rotations (index of the minimum element).
    """
    n = len(arr)
    low, high = 0, n - 1

    # The loop continues until the search space is exhausted (low > high).
    while low <= high:
        # Case 1: If the subarray is already sorted, return the index of the first element
        if arr[low] < arr[high]:
            return low
        
        mid = (low + high) // 2
        next_idx = (mid + 1) % n            # Index of the next element (wraps around)
        prev_idx = (mid - 1 + n) % n        # Index of the previous element (wraps around)

        # Case 2: Check if mid is the minimum element
        # The minimum element is the only element that is smaller than its previous and next elements.
        if arr[mid] < arr[next_idx] and arr[mid] < arr[prev_idx]:
            return mid

        # Case 3: Decide which half to search next
        # If mid is greater than high, it means the right half is disrupted/unsorted, meaning the minimum is there.
        if arr[mid] > arr[high]: 
            low = mid + 1          # Search in the right half
        else:
        # arr[mid] < arr[high]
        # If mid is less than high, it means the right half is sorted, so the minimum must be in the left half.
            high = mid - 1         # Search in the left half
                
    return -1  # This line should never be reached if input is valid; signals a problem if hit this line


### Why This Code Works ###
# Your code covers all the critical edge cases beautifully:
# 1. Already Sorted Array (0 rotations): arr[low] < arr[high] immediately catches this and returns 0.
# 2. Modulo Wraparound: Your next_idx and prev_idx handling ensures that if the minimum element is at index# 0 or index n-1, the code won't throw an IndexError.
# 3. Halving the Search Space: The logic correctly identifies which side is unrotated/sorted (meaning the "pivot" or minimum element lies on the other, disrupted/unsorted side).

arr = [2, 1]
print(rotation_count_binary(arr))  # Output: 1




### Changing comparison operators from <= and >= to strict < and > ###
# Changing the comparison operators from <=" or >=" to strict < or > makes sense on the surface since the elements are unique.
# However, you accidentally removed a critical component of standard binary search: handling the case when "mid == low".
# Here is exactly where and why the code breaks.

# The Bug:      When mid == low
# When your search space shrinks down to two elements (e.g., low is 0 and high is 1), the midpoint calculation (0 + 1) // 2 evaluates to 0.
# Because mid is now exactly equal to low, evaluating arr[mid] > arr[low] checks if an element is strictly greater than itself (e.g., arr[0] > arr[0]). 
# This is always false. 
# Because it evaluates to false, your code drops straight into the else block: 
#               else:                   # Right half is sorted
#                   high = mid - 1      # Search in the left half

# This forces high = 0 - 1 = -1. The loop terminates, and the function returns -1 (an error), completely missing the correct element.

# A Concrete Example: arr = [2, 1] (rotated 1 time)
# Let's trace your rewritten code with this input:
# 1. low = 0, high = 1, n = 2
# 2. arr[low] < arr[high] → 2 < 1 is False.
# 3. mid = (0 + 1) // 2 = 0
# 4a. next_idx = (mid + 1) % n = (0 + 1) % 2 = 1
# 4b. prev_idx = (mid - 1 + n) % n = (0 - 1 + 2) % 2 = 1
# 5. arr[mid] < arr[next_idx] → 2 < 1 is False (Case 2 skipped).
# 6. if arr[mid] > arr[low]:    →   arr[0] > arr[0]     →   2 > 2 is False.
# 7. Code hits the else block: high = mid - 1 = 0 - 1 = -1.
# 8. Loop ends because low <= high (0 <= -1) is False.
# 9. Returns -1. The correct answer was 1.

# The Fix
# If you want to use strict inequalities for comparing elements because they are unique, you still must account for index identity when mid == low.
# You can safely change your if/else checks to use strict inequalities, but you have to modify the condition to look at:
#                 arr[mid] >= arr[low] (or handle mid == low explicitly).

# The safest and cleanest way to keep strict element comparisons while fixing the index issue is to compare mid against high instead:

        # Case 3: Decide which half to search next
        # If mid is greater than high, the right side is disrupted, meaning the minimum is there.
        
        # Code:
        # if arr[mid] > arr[high]: 
        #    low = mid + 1          # Search in the right half
        # else:                      
        #    high = mid - 1         # Search in the left half

# Summary of what works with strict inequality:
# • Case 1 (arr[low] < arr[high]): This change is actually perfectly fine! Because the elements are unique, a sorted subarray will always have arr[low] < arr[high].
# • Case 2 (arr[mid] < arr[next_idx] ...): This is also fine, as unique elements will never be equal.
# • Case 3 (arr[mid] > arr[low]): This is what broke the code due to index overlap. Changing it to compare mid with high avoids the overlap issue entirely because when there are two elements left, mid equals low, meaning mid never equals high.





### Why the fix of the bug is as such ###
# It all comes down to which boundary you are overlapping with when the search space shrinks.
# When you have only 2 elements left in a binary search, mid will always equal low due to integer division dropping the remainder (e.g., (0 + 1) // 2 = 0).
# Because mid == low, they point to the exact same element. 
# Therefore, comparing arr[mid] to arr[low] means you are comparing an element to itself. 
# A number is never strictly greater than itself, which breaks your logic.
# By comparing arr[mid] against arr[high], you ensure you are always comparing two completely different elements, 
# because mid can never equal high when there are 2 elements left.

# Side-by-Side Comparison
# Let's trace both approaches using the exact same breaking input from before: arr = [2, 1] (a sorted array rotated 1 time).
# • Setup for both: low = 0, high = 1, mid = (0 + 1) // 2 = 0
# • arr[mid] is arr[0] (value 2)
# • arr[low] is arr[0] (value 2)
# • arr[high] is arr[1] (value 1)

# Strategy A: Comparing mid against low (Broken)
# The Code:
#           if arr[mid] > arr[low]:    
#               low = mid + 1
#           else:
#           # arr[mid] < arr[low]      
#               high = mid - 1

# Evaluation:   Evaluates arr[0] > arr[0] → 2 > 2.
# Result:       2 > 2 is False.
# Action Taken: 
# It falls into the else block:
#           high = mid - 1
#           high = 0 - 1 = -1
# Outcome:  The loop ends because low <= high (0 <= -1) is False.❌ 
# Returns -1 (Bug)





# Strategy B: Comparing mid against high (Fixed)
# The Code:
#           if arr[mid] > arr[high]:
#               low = mid + 1
#           else:
#           # arr[mid] < arr[high] 
#               high = mid - 1

# Evaluation:Evaluates arr[0] > arr[1] → 2 > 1.
# Result:2 > 1 is True.
# Action Taken:
# It executes the if block:
#           low = mid + 1
#           low = 0 + 1 = 1
# Our array is arr = [2, 1] (n = 2).
# • low is now 1
# • high is still 1
# The loop condition while low <= high evaluates to 1 <= 1, which is True, so we enter the loop.

# Step 2: The Two Paths to Victory
# Depending on how your code is ordered, it will successfully return 1 in one of two ways. In your actual code, Case 1 runs first, but let's look at how both conditions safely catch it:

# Path A: Caught by Case 1 (The Array check)
# Your code first checks if the current subarray is sorted:
#           if arr[low] < arr[high]:
#               return low

# Since low is 1 and high is 1, this checks arr[1] < arr[1] (→ 1 < 1), which is False.
# Because Case 1 is false, the code moves down to calculate mid:
#           mid = (low + high) // 2 = (1 + 1) // 2 = 1
# Now that mid = 1, it hits Path B.

# Path B: Caught by Case 2 (The Neighbor check)
# Next, the code calculates the neighbor indices using your modulo wraparound formula (n = 2):
# • next_idx = (1 + 1) % 2 = 0
# • prev_idx = (1 - 1 + 2) % 2 = 0
# Then it evaluates Case 2:
#           if arr[mid] < arr[next_idx] and arr[mid] < arr[prev_idx]:
#               return mid

# Plugging in our values (mid = 1, next_idx = 0, prev_idx = 0):
# • Is arr[mid] < arr[next_idx] → Is arr[1] < arr[0]? → 1 < 2 is True.
# • Is arr[mid] < arr[prev_idx] → Is arr[1] < arr[0]? → 1 < 2 is True.
# Since both are True, the condition passes, and the code executes return mid, which returns 1.

# Summary of the Note
# When I wrote "If Case 1 doesn't catch it immediately...", I was highlighting that even though Case 1 evaluates to False 
# (because a single element arr[1] isn't strictly less than itself), the binary search doesn't break. 
# It safely proceeds to calculate mid = 1, allows Case 2 to realize that arr[1] is smaller than its neighbor arr[0], 
# and successfully returns the correct rotation count of 1.






# Outcome:  The loop continues because low <= high (1 <= 1) is True.
# Next iteration catches arr[low] < arr[high] (Case 1) or Case 2, correctly returning 1.
# Note: If Case 1 doesn't catch it immediately, mid becomes 1. 
# Then Case 2 sees arr[1] is smaller than its neighbors, returning index 1.
# ✓ Returns 1 (Correct)

# Why Strategy B works for all states:
# If arr[mid] > arr[high], it proves the array is disrupted somewhere between mid and high (because in a normal sorted array, elements get bigger as you go right).
# A disruption means the inflection point/minimum element must be sitting in that right half. Moving low = mid + 1 safely hunts it down.






### The following code below is code that has the Bug (for your reference only). ###
### because it compares "mid" against "low" instead of "mid" against "high". ###
### The code syntax is correct but it will not work when the search space shrinks to 2 elements, e.g. arr = [2, 1] (rotated 1 time) ###
### because mid == low, and arr[mid] > arr[low] will always be false. ###
### so the code will fall into the else block and set high = mid - 1, which will terminate the loop and return -1. ###
### refer to the above explanation (Strategy A) for a detailed breakdown of why this happens. ###    

# Case 3: Decide which half to search next
# arr[mid] > arr[low] indicates that the left half is sorted, so we search in the right half.

#       if arr[mid] > arr[low]:  # Left half is sorted
#           low = mid + 1          # Search in the right half

# arr[mid] < arr[low]
# If mid is less than low, it means the left half is disrupted/unsorted, meaning the minimum is there.

#       else:
#           high = mid - 1         # Search in the left half