### Question: Handling repeating numbers ###

# So far we've assumed that the numbers in the list are unique. What if the numbers can repeat? 
# E.g. `[5, 6, 6, 9, 9, 9, 0, 0, 2, 3, 3, 3, 3, 4, 4]`. 
# Can you modify your solution to handle this special case?

### End of Question ###



def rotation_count_duplicates(arr):
    low = 0
    high = len(arr) - 1
    
    while low < high:
        mid = (low + high) // 2
        
        # If the mid element is greater than the high element, the rotation point is to the right
        if arr[mid] > arr[high]:
            low = mid + 1
        # If the mid element is less than the high element, the rotation point is to the left
        elif arr[mid] < arr[high]:
            high = mid
        else:
            # If arr[mid] == arr[high], we can't determine the side, reduce high by 1
            high -= 1
            
    return low

### Test cases ###
arr = [5, 6, 6, 9, 9, 9, 0, 0, 2, 3, 3, 3, 3, 4, 4]
print(rotation_count_duplicates(arr))  # Output: 6 (the index of the smallest element, which is 0)

### Dry Run ###
# arr = [5, 6, 6, 9, 9, 9, 0, 0, 2, 3, 3, 3, 3, 4, 4]

# Iteration 1:
# Indexes: low = 0 (value "5"), high = 14 (value "4")
# Index: mid = (0 + 14) // 2 = 7 (value "0")
# Since arr[mid] < arr[high] (0 < 4) → Case 2 triggers: we set high = mid = 7.

# Iteration 2:
# Indexes: low = 0 (value "5"), high = 7 (value "0")
# Index: mid = (0 + 7) // 2 = 3 (value "9")
# Since arr[mid] > arr[high] (9 > 0) → Case 1 triggers: we set low = mid + 1 = 3 + 1 = 4.

# Iteration 3:
# Indexes: low = 4 (value "9"), high = 7 (value "0")
# Index: mid = (4 + 7) // 2 = 5 (value "9")
# Since arr[mid] > arr[high] (9 > 0) → Case 1 triggers: we set low = mid + 1 = 5 + 1 = 6.

# Iteration 4:
# Indexes: low = 6 (value "0"), high = 7 (value "0")
# Index: mid = (6 + 7) // 2 = 6 (value "0")
# Since arr[mid] == arr[high] (0 == 0) → Case 3 triggers: we set high = high - 1 = 7 - 1 = 6.

# Iteration 5:
# Indexes: low = 6 (value "0"), high = 6 (value "0")
# The "while" loop terminates since low == high. (low is no longer less than high, 6 < 6 is False.)
# Returns low = 6
# Index 6 is the first 0 in your array, meaning the array was rotated to the right 6 times. The code works perfectly!



### Q & A ###
# 1. Why can't it be "while low <= high" instead of "while low < high"?

# Answer
# Using "while low <= high" could lead to an infinite loop in cases where the array has duplicates, as the condition may not allow the loop to terminate correctly when low and high converge.
# The "while low < high" condition ensures that the search space is reduced appropriately and avoids unnecessary comparisons when low equals high.

# arr = [5, 6, 6, 9, 9, 9, 0, 0, 2, 3, 3, 3, 3, 4, 4]


### Things to consider:
# 1. The algorithm still runs in O(log n) time complexity in the average case
# 2. In the worst case, when there are many duplicates, the time complexity can degrade to O(n) because we may have to check each element when arr[mid] == arr[high].
# 3. The function returns the index of the smallest element, which indicates how many times the array has been rotated.
# 4. This approach works for arrays with repeated numbers, as it handles the case where arr[mid] == arr[high] by decrementing high, allowing us to continue searching for the rotation point.
# 5. The function can be tested with various cases, including arrays with all identical elements, arrays with no rotation, and arrays with multiple rotations to ensure robustness.
# 6. The function can also be modified to return the number of rotations directly by returning the index of the smallest element, which is equivalent to the number of rotations in a sorted array.
# 7. The function can be further optimized or modified to handle edge cases, such as empty arrays or arrays with a single element, by adding appropriate checks at the beginning of the function.
# 8. The function can be extended to handle arrays that are sorted in descending order or arrays that are not strictly increasing, by adjusting the comparison logic accordingly.
# 9. The function can be integrated into larger applications or systems that require efficient handling of rotated sorted arrays with duplicates, such as search algorithms, data analysis tools, or real-time systems.
# 10. The function can be documented with clear explanations of its parameters, return values, and potential exceptions to improve usability and maintainability for future developers or users.


arr = [3,4,5,6,7,0,1,2]
left = 0 (value "3")
right = len(arr) - 1 = 7 (value "2")
mid = (left + right) // 2 = 3 (value "6")

target = value "0"
left < mid → this means that the left half of the array is sorted. Since the target value "0" is not in the range of the left half (3 to 6), we can discard the left half and search in the right half.

left = mid + 1 = 4 (value "7")
right = 7 (value "2")
