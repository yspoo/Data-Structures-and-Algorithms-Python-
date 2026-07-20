### Question ###

# There is an integer array nums sorted in ascending order (with distinct values). All values of nums are unique.
# Prior to being passed to your function, nums is possibly left rotated at an unknown index k (1 <= k < nums.length)
# such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). 
# For example, [0,1,2,4,5,6,7] might be left rotated by 3 indices and become [4,5,6,7,0,1,2].

# Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums,
# or -1 if it is not in nums.

# You must write an algorithm with O(log n) runtime complexity.

# Example 1:
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4

# Example 2:
# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1

# Example 3:
# Input: nums = [1], target = 0
# Output: -1

### End of Question ###

def search(nums, target):
    '''
    This function searches for a target (target) value in a rotated increasing order sorted array (nums) using modified binary search.
    It returns the index of the target if found, otherwise returns -1.
    The algorithm runs in O(log n) time complexity.

    Parameters:
    nums (List[int]): A list of integers sorted in ascending order and possibly rotated.
    target (int): The integer value to search for in the array.

    Returns:
    int: The index of the target in the array if found, otherwise -1.
    '''
    low = 0
    high = len(nums) - 1
    
    # Perform binary search while the low index is less than or equal to the high index
    # If low index is greater than high index, it means the target is not present in the array
    while low <= high:

        # Calculate the mid index
        mid = (low + high) // 2
        
        # Check if the mid element is equal to the target
        # If it is, return the mid index as the target is found
        # If not, determine which side of the array is sorted and adjust the search range accordingly
        if nums[mid] == target:
            return mid
        
        # Determine which side is sorted
        # If the left side is sorted, check if the target is within that range
        # If it is, adjust the high index to search in the left side
        # If not, adjust the low index to search in the right side
        if nums[low] <= nums[mid]:  # Left side is sorted
            
            # Check if the target is within the sorted left side
            if nums[low] <= target < nums[mid]:  # If true, target is in the left side
                
                # Adjust the high index to mid - 1 to search in the left side
                high = mid - 1
            
            # If the target is not in the sorted left side, it must be in the right side
            # Adjust the low index to mid + 1 to search in the right side
            else:  # Target is in the right side
                low = mid + 1

        # If the left side is not sorted, then the right side must be sorted
        # Check if the target is within the sorted right side
        # If it is, adjust the low index to search in the right side
        # If not, adjust the high index to search in the left side
        else:  # Right side is sorted

            # Check if the target is within the sorted right side
            if nums[mid] < target <= nums[high]:  # If true, target is in the right side

                # Adjust the low index to mid + 1 to search in the right side
                low = mid + 1

            # If the target is not in the sorted right side, it must be in the left side
            # Adjust the high index to mid - 1 to search in the left side
            else:  # Target is in the left side
                high = mid - 1

    # If the loop ends and the target is not found, return -1 to indicate that the target is not present in the array
    return -1


### Test cases ###
# Example 1 #
nums1 = [4,5,6,7,0,1,2]
target1 = 0
print(search(nums1, target1))  # Output: 4

# Example 2 #
nums2 = [4,5,6,7,0,1,2]
target2 = 3
print(search(nums2, target2))  # Output: -1

# Example 3 #
nums3 = [1]
target3 = 0
print(search(nums3, target3))  # Output: -1

# Example 4 #
nums4 = [3,4,5,6,7,0,1,2]
target4 = 0
print(search(nums4, target4))  # Output: 5

# Example 5 #
nums5 = [6,7,0,1,2,3,4,5]
target5 = 7
print(search(nums5, target5))  # Output: 1

# See this video to understand the code above: https://www.youtube.com/watch?v=6WNZQBHWQJs
