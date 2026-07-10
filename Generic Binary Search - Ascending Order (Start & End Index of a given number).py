# Question (Leetcode Exercise 34):

# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
# If target is not found in the array, return [-1, -1].
# You must write an algorithm with O(log n) runtime complexity.

# Example 1:
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]

# Example 2:
# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]

# Example 3:
# Input: nums = [], target = 0
# Output: [-1,-1]
 

def binary_search(lo, hi, condition_received):
    '''
    Performs binary search on a sorted increasing array to find the index of an element that satisfies a given condition.
    
    Args:
        lo (int): The lower bound of the search range.
        hi (int): The upper bound of the search range.
        condition_received (function): A function that takes an index and returns 'found', 'left', or 'right'.
    
    Returns:
        int: The index of the element that satisfies the condition, or -1 if not found.
    '''
    
    # The loop continues as long as there is a valid search range left to look through.
    while lo <= hi:
        # Calculates the middle index of the current search range, rounding down to the nearest integer.
        mid = (lo + hi) // 2
        # Calls the condition_received function on the middle index to determine the next step in the search.
        result = condition_received(mid)
        if result == 'Found':
            return mid
        # If the received condition indicates that the target is to the left of mid, adjust the upper bound to mid - 1.
        elif result == 'Left':
            hi = mid - 1
        # If the received condition indicates that the target is to the right of mid, adjust the lower bound to mid + 1.
        else:
        # elif result == 'Right':
            lo = mid + 1
    # If the loop ends and lo > hi, it means the number wasn't found in the array/list. Return -1.
    return -1

# Function to find the first occurrence of the target
def first_position(nums, target):
    # An inner helper function designed specifically for finding the first occurrence.
    def condition(mid):
        # Checks if the middle element is equal to the target.
        if nums[mid] == target:
            # If the middle index is greater than 0 and the previous element (nums[mid-1]) is also equal to the target, 
            # it means we haven't found the first occurrence yet. Return "Left" to continue searching in the left half.
            if mid > 0 and nums[mid-1] == target:
                return "Left"
            # If the middle index is 0 or the previous element (nums[mid-1]) is not equal to the target, it means we've found the first occurrence. Return "Found".
            return "Found"
        # If the middle element is less than the target, it means the target must be in the right half of the array.
        # Return "Right" to continue searching in the right half.
        elif nums[mid] < target:
            return "Right"
        else:
        # elif nums[mid] > target:
        # If the middle element is greater than the target, it means the target must be in the left half of the array.
        # Return "Left" to continue searching in the left half.
            return "Left"
    # Starts the binary search from index 0 to the last index of the list, passing our specialized first-occurrence condition.
    return binary_search(0, len(nums)-1, condition)

# Function to find the last occurrence of the target
def last_position(nums, target):
    # An inner helper function designed specifically for finding the last occurrence.
    def condition(mid):
        # Checks if the middle element is equal to the target.
        if nums[mid] == target:
            # If the middle index is less than the last index and the next element (nums[mid+1]) is also equal to the target,
            # it means we haven't found the last occurrence yet. Return "Right" to continue searching in the right half.
            if mid < len(nums)-1 and nums[mid+1] == target:
                return "Right"
            return "Found"
        # If the middle element is less than the target, it means the target must be in the right half of the array.
        # Return "Right" to continue searching in the right half.
        elif nums[mid] < target:
            return "Right"
        else:
        # elif nums[mid] > target:
        # If the middle element is greater than the target, it means the target must be in the left half of the array.
        # Return "Left" to continue searching in the left half.
            return "Left"
        # Starts the binary search from index 0 to the last index of the list, passing our specialized last-occurrence condition.
    return binary_search(0, len(nums)-1, condition)
    
def first_and_last_position(nums, target):
    # Calls the first_position function to find the first occurrence of the target.
    first = first_position(nums, target)
    # Calls the last_position function to find the last occurrence of the target.
    last = last_position(nums, target)
    # Returns a list containing the indices of the first and last occurrences of the target.
    return [first, last]

### Test Cases ###
nums, target = [5,7,7,8,8,10], 8
print(first_and_last_position(nums, target))  # Output: [3, 4]

nums, target = [5,7,7,8,8,10], 6
print(first_and_last_position(nums, target))  # Output: [-1, -1]

nums, target = [], 0
print(first_and_last_position(nums, target))  # Output: [-1, -1]