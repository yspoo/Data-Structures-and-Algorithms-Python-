### Question: ###

# You are given list of numbers, obtained by rotating a sorted list an unknown number of times. 
# Write a function to determine the minimum number of times the original sorted list was rotated to obtain the given list. 
# Your function should have the worst-case complexity of O(log N), where N is the length of the list. You can assume that all the numbers in the list are unique.

# Example: The list [5, 6, 9, 0, 2, 3, 4] was obtained by rotating the sorted list [0, 2, 3, 4, 5, 6, 9] 3 times.

# We define "rotating a list" as removing the last element of the list and adding it before the first element. E.g. rotating the list [3, 2, 4, 1] produces [1, 3, 2, 4].

# "Sorted list" refers to a list where the elements are arranged in the increasing order e.g. [1, 3, 5, 7].

### End of Question ###


### Concept ###
# Suppose our original sorted list is [1, 3, 5, 6, 7]
# When k = 2, we get: [6, 7, 1, 3, 5]
# The starting element (index 0) in the original sorted list is 1, which is at index 2 in the rotated list. Therefore, the minimum number of rotations is 2.

# If a list of sorted numbers is rotated k times, then the smallest number in the list ends up at position k (counting from 0). 
# Further, it is the only number in the list which is smaller than the number before it. 
# Thus, we simply need to check for each number in the list whether it is smaller than the number that comes before it (if there is a number before it). 
# Then, our answer i.e. the number of rotations is simply the position of this number is . If we cannot find such a number, then the list wasn't rotated at all.

# Example: In the list [19, 25, 29, 3, 5, 6, 7, 9, 11, 14], the number 3 is the only number smaller than its predecessor. 
# It occurs at the position 3 (counting from 0), hence the array was rotated 3 times.

# We can use the linear search algorithm as a first attempt to solve this problem i.e. we can perform the check for every position one by one.

# Describe the linear search solution explained above problem in your own words:
# 1. Create a variable position with value 1 (because we want to compare the current position with the previous position, so we start from index 1).
# 2. Compare the number at the current position with the number at the previous position.
# 3. If the number at the current position is smaller than the number at the previous position, return the current position as the number of rotations.
# 4. If the current position is not smaller than the previous position, increment the position by 1 and repeat step 2.
# 5. If we reach the end of the list without finding a number smaller than its predecessor, return 0 as the list was not rotated.
# 6. The time complexity of this linear search solution is O(N) in the worst case, where N is the length of the list. This is because we may have to check every element in the list to find the minimum number of rotations.
# 7. The space complexity of this solution is O(1) as we are using a constant amount of extra space regardless of the input size.
# 8. The linear search solution is simple to implement and understand, but it is not efficient for large lists as it has a linear time complexity.
# 9. The linear search solution can be improved to achieve a logarithmic time complexity of O(log N) by using a binary search approach. This is because the list is sorted and rotated, which allows us to eliminate half of the search space at each step.

### End of Concept ###



### Linear Search Solution ###
def count_rotations_linear(nums):
    # Here, we set "position" variable to 0 even though we said we will check from index 1. 
    # This is because we can start counting from index 0 because when position == 0, we will skip the "if" condition and instead position will be incremented by 1.
    # So it makes no difference whether we start from index 0 or index 1.
    # But it is good practice to start from index 0 if possible whenver you iterate over a list, because it makes the code more readable and understandable.
    # This is also because we want to return the position of the minimum number, which is at index 0 if the list is not rotated.
    position = 0

    # We will check for each number in the list whether it is smaller than the number that comes before it (if there is a number before it).
    while position < len(nums):
        if position > 0 and nums[position] < nums[position - 1]:
            return position
        
        # If the current position is not smaller than the previous position, increment the position by 1 and repeat the check.
        position += 1
    
    # If we reach the end of the list without finding a number smaller than its predecessor, return 0 as the list was not rotated.
    # The list could have also been rotated a multiple of its length, in which case it would look the same as the original sorted list.
    # Therefore, we return 0 in this case as well.
    # Because the number of rotations is always taken modulo the length of the list, so if the list was rotated a multiple of its length, it would be equivalent to 0 rotations.
    # The Mathematical Formula:                 
    #                               Effective Rotations = Total Rotations % N, where N is the length of the list.
    
    # The algorithm can only find the effective rotations (the index of the minimum element).
    # If an interview question says, "An array of size 5 was rotated 12 times, what does it look like?", you immediately simplify it using modulo: 12 % 5 = 2. 
    # You only need to simulate 2 rotations.
    # For more information, see the Extra Information section of the assignment.
    return 0



### Extra Information ###
# 1. The Full-Cycle Example (Rotations equal to length)
# Let's take a list of length 4: [1, 2, 3, 4]
# 0 Rotations: [1, 2, 3, 4]
# 1 Rotation:  [4, 1, 2, 3]
# 2 Rotations: [3, 4, 1, 2]
# 3 Rotations: [2, 3, 4, 1]
# 4 Rotations: [1, 2, 3, 4] (We are right back to the start!)
# Mathematically, 4 % 4 = 0. 
# The array index of the minimum element (1) is 0. 
# We cannot look at the list [1, 2, 3, 4] and tell if it was rotated 0 times, 4 times, or 400 times—visually and structurally, it is 0 effective rotations.

# 2. The Over-Rotation Example (Rotations greater than length)
# Imagine you are given the array [3, 4, 1, 2] and told it was rotated 14 times to the right.
# Let's apply the modulo rule where length N = 4: 14 % 4 = 2
# This tells us that rotating a 4-element list 14 times produces the exact same result as rotating it just 2 times.
# Cycle 1 (4 rotations): Lands back at [1, 2, 3, 4]
# Cycle 2 (8 rotations): Lands back at [1, 2, 3, 4]
# Cycle 3 (12 rotations): Lands back at [1, 2, 3, 4]
# Remaining 2 rotations (14 total): Lands at [3, 4, 1, 2]
# When we run our code on [3, 4, 1, 2], the minimum element 1 is at index 2.
# The code correctly returns 2 because it is physically impossible to know about the 12 "extra" rotations just by looking at the final array.

# Linear Search Time Complexity: O(N)