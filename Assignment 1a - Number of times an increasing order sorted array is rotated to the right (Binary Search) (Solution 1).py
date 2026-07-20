### Question: ###

# You are given list of numbers, obtained by rotating a sorted list an unknown number of times. 
# Write a function to determine the minimum number of times the original sorted list was rotated to obtain the given list. 
# Your function should have the worst-case complexity of O(log N), where N is the length of the list. You can assume that all the numbers in the list are unique.

# Example: The list [5, 6, 9, 0, 2, 3, 4] was obtained by rotating the sorted list [0, 2, 3, 4, 5, 6, 9] 3 times.

# We define "rotating a list" as removing the last element of the list and adding it before the first element. E.g. rotating the list [3, 2, 4, 1] produces [1, 3, 2, 4].

# "Sorted list" refers to a list where the elements are arranged in the increasing order e.g. [1, 3, 5, 7].

### End of Question ###



### Concept ###
# When applying binary search to find the rotation count (which is the index of the minimum element), the array structure changes depending on how it was handled.
# To write a foolproof solution, you have to account for specific edge cases.

# The 4 Cases to Account For
# Before looking at the code, we need to understand the scenarios our binary search will encounter:





# Case 1: The array is not rotated at all (or rotated a multiple of its length)
# Example: [1, 2, 3, 4, 5]
# Behavior: The array is already perfectly sorted. The first element is smaller than the last element (arr[low] < arr[high]). If we detect this, we can immediately return low (0) without searching.





# Case 2: The middle element itself is the pivot point
# This happens at the boundary where the rotation occurred.

# 1. What is the "Pivot Point"?
# In a normal, strictly increasing sorted list, every single element is smaller than the element to its right (index 0 < index 1 < index 2 < index 3).
# The pivot point is the exact location where this rule is broken. It is the boundary where the numbers suddenly drop from the maximum value back down to the minimum value.
# Because it represents this sudden drop, the pivot point is always the absolute minimum element of the array.

# 2. What is "the boundary where the rotation occurred"?
# Imagine a rubber band representing our sorted list: [1, 2, 3, 4, 5].

# If we "cut" the list between the 3 and the 4, and shift the right piece to the front, we get: [4, 5 | 1, 2, 3]
# That vertical line | is the boundary where the rotation occurred.
# To the left of the boundary ([4, 5]), the numbers are perfectly sorted.
# To the right of the boundary ([1, 2, 3]), the numbers are perfectly sorted.
# At the boundary itself, 5 connects to 1. This is the structural anomaly. The number 1 is the pivot point because it sits right on the edge of that rotation cut.

# When I stated that “the middle element itself is the pivot point,” I meant that during our binary search, our calculated mid index lands exactly on one of the elements right next to that rotation cut.

# Let's look at the two ways mid can land on this boundary:
# Scenario A: mid lands exactly on the Minimum ElementTake the array: [4, 5, 1, 2, 3]
# low is index 0 (4), high is index 4 (3).
# Calculate mid: (0 + 4) // 2 = index 2. arr[mid] is 1.
# Here, mid is sitting exactly on the pivot point (the minimum).
# We can instantly verify this because its left neighbor (5) is greater than it.
# In a normal sorted array, a left neighbor should never be greater.

# Scenario B: mid lands exactly on the Maximum Element
# Let's look at an array shifted slightly differently: [3, 4, 5, 1, 2]
# low is 0 (3), high is 4 (2). mid is index 2, which is 5.
# Here, mid is sitting on the maximum element, right before the rotation cut.
# We can instantly identify the pivot point because its right neighbor (1) is smaller than it.
# A right neighbor should never be smaller in an increasing list.
# Therefore, mid + 1 (index 3) is our pivot point.

# The pivot point is just a technical nickname for the minimum element in a rotated array,
# and the boundary is the seam where the end of the original array was glued to the front of the original array.
# Case 2 simply highlights the moments in binary search where our midpoint lands right on that seam, allowing us to finish the search immediately.

# We can identify this by checking if the middle element is less than its previous element (arr[mid] < arr[mid - 1])
# or greater than its next element (arr[mid] > arr[mid + 1]). 
# If either condition is true, we have found the minimum element. 

# There are two sub-cases here:
# The mid element is the minimum: [4, 5, 1, 2, 3]. Here, mid is at index 2 (1). We can identify this because arr[mid] < arr[mid - 1].
# The mid element is the maximum: [5, 1, 2, 3, 4]. Here, mid is at index 0 (5). The element right next to it (arr[mid + 1]) is the minimum. We can identify this because arr[mid] > arr[mid + 1].





# Case 3: The minimum element is in the right half
# Example: [4, 5, 6, 1, 2] (where mid is at index 2, value 6)
# Behavior: If arr[mid] > arr[high], it proves the natural sorted order is broken in the right half. The "drop-off" point (minimum element) must be to the right of mid. We discard the left half.





# Case 4: The minimum element is in the left half
# Example: [5, 1, 2, 3, 4] (where mid is at index 2, value 2)
# Behavior: If arr[mid] < arr[high], the right half is perfectly sorted in increasing order. Therefore, the minimum element cannot be in the strictly increasing right half (unless mid itself is the minimum). We discard the right half and keep searching the left half.

### End of Concept ###



# This function counts the number of times a sorted array has been rotated to the right.
# It uses a modified binary search approach to find the index of the minimum element, which corresponds to the number of rotations.
# The function handles edge cases, such as an empty list, and efficiently narrows down the search space based on comparisons between the middle element and its neighbors.
def count_rotations(arr):
    # We set "n" to the length of the array to avoid recalculating it multiple times.
    # We will use this value "n" to determine the indices of the next and previous elements in a circular manner.
    n = len(arr)
    
    # Edge Case: Empty list. (An empty list cannot be rotated, so we gracefully exit with 0.)
    if n == 0:
        return 0
        
    # We establish our search boundaries at the very beginning and very end of the list.
    low = 0
    high = n - 1
    
    # We enter a loop that continues as long as our search space is valid (i.e., low index is less than or equal to high index).
    while low <= high:
        # Case 1: If the current subspace is already sorted, then arr[low] must be the minimum element.
        if arr[low] <= arr[high]:
            return low
            
        mid = (low + high) // 2
        next_idx = (mid + 1) % n            # (see below for explanation)
        prev_idx = (mid - 1 + n) % n        # (see below for explanation)
        
        # Case 2a: Check if mid + 1 is the minimum element
        if arr[mid] > arr[next_idx]:
            return next_idx
            
        # Case 2b: Check if mid itself is the minimum element
        if arr[mid] < arr[prev_idx]:
            return mid
            
        # Case 3: If mid element is greater than the high element, the minimum element lies in the right half.
        if arr[mid] > arr[high]:
            low = mid + 1

        # Case 4: Otherwise, the minimum lies in the left half.
        # We adjust the high index to mid - 1 to narrow our search space.
        # This is because if arr[mid] is less than or equal to arr[high], it indicates that the right half is sorted, and thus the minimum must be in the left half.
        # We continue this process until we find the minimum element, which gives us the count of rotations.
        else:
            high = mid - 1
            
    return 0




### Understanding "next_idx = (mid + 1) % n" and "prev_idx = (mid - 1 + n) % n" ###
# These two lines look confusing because they are doing a bit of clever math to solve a classic coding problem: index wrapping.
# They ensure that no matter where mid is in the list, calculating its neighbors will never crash your program with an IndexError. 
# Instead of going out of bounds, the index gently loops back around to the other side of the list.
# Here is the breakdown of why they are written this way.

# The Goal: Creating a Circular List
# In your binary search, you need to check the numbers right next to mid.
# Usually, mid + 1 is the next item, and mid - 1 is the previous item.
# But what happens if mid is the very last item in the list? mid + 1 falls off the right edge.
# What if mid is the very first item (index 0)? mid - 1 becomes -1, falling off the left edge.
# The modulo operator (% n) forces the index to wrap around circularly, treating the list like a loop.

# 1. Explaining "next_idx = (mid + 1) % n"
# This line finds the index of the next element, wrapping back to 0 if we go past the end.
# Imagine a list of size n = 5 (indices 0, 1, 2, 3, 4).
# If mid = 2 (middle of the list): (2 + 1) = 3 % 5 = 3 (Normal behavior. Index 3 is the next item).
# If mid = 4 (the very last item): (4 + 1) = 5 % 5 = 0 (Magical wrap-around! Instead of crashing at index 5, it cleanly circles back to index 0).

# 2. Explaining "prev_idx = (mid - 1 + n) % n"
# This line finds the index of the previous element, wrapping to the very last index if we go past the beginning.
# You might wonder: Why can't we just do (mid - 1) % n?
# In Python, (-1) % 5 actually does equal 4, but adding + n is an explicit, cross-language safety habit. 
# It guarantees the number inside the parentheses is positive before applying the modulo, preventing weird behavior in languages like C++ or Java.
# Let's look at how it works with n = 5:
# If mid = 2 (middle of the list): (2 - 1 + 5) = 6 % 5 = 1 (Normal behavior. Index 1 is the previous item).
# If mid = 0 (the very first item): (0 - 1 + 5) = 4 % 5 = 4 (Magical wrap-around! Instead of a negative number, it safely points to index 4, the last item in the list).

# Summary Checklist
# If mid is at          mid + 1 behaves like            mid - 1 + n behaves like
# Middle                Just moves right (+1)           Just moves left (-1)
# End of list           Wraps to the start (0)          Just moves left (-1)
# Start of list         Just moves right (+1)           Wraps to the end (n - 1)
# By using these formulas, your binary search can confidently look at neighbors without needing a bunch of messy if/else statements to check if it's hitting the edges of the list.



### Understanding the Algorithm ###
# The algorithm uses a modified binary search to find the index of the minimum element in a rotated sorted array.
# The index of the minimum element corresponds to the number of times the array has been rotated to the right.
# The algorithm handles edge cases, such as an empty list, 
# and efficiently narrows down the search space based on comparisons between the middle element and its neighbors. 
  


### Understanding the Space Complexity of the Algorithm ###
# The space complexity of this algorithm is O(1), which means it uses a constant amount of extra space regardless of the input size.
# This is because we are only using a fixed number of variables (low, high, mid, next_idx, prev_idx) to keep track of our search space and indices,
# and we are not using any additional data structures that grow with the input size.



### Understanding the Time Complexity of the Algorithm ###
# The time complexity of this algorithm is O(log n), where n is the number of elements in the array.
# This is because we are using a binary search approach, which divides the search space in half with each iteration.
