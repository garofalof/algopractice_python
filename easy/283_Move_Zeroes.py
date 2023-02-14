from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        pointer = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[pointer] = nums[pointer], nums[i]
                pointer += 1


"""
Explanation:

Use a pointer to keep track of the position of the next non-zero element in the list. For each iteration, check if the current element is not zero. If it's not, swap the current element with the element at the position pointed by the pointer, and increment the pointer by one. This process continues until all non-zero elements are moved to the left side of the list and all zeros are moved to the right side.

Notes:

Time Complexity: O(n)

Space Complexity: O(1)
"""

# Test 1: Single element is 0
list = [0]
expected = [0]
Solution().moveZeroes(list)
moved_list = list
assert moved_list == expected, f"Expected {expected} but got {moved_list}"

# Test 2: Single element is not 0
list = [1]
expected = [1]
Solution().moveZeroes(list)
moved_list = list
assert moved_list == expected, f"Expected {expected} but got {moved_list}"

# Test 3: Multiple elements all 0
list = [0, 0, 0, 0]
expected = [0, 0, 0, 0]
Solution().moveZeroes(list)
moved_list = list
assert moved_list == expected, f"Expected {expected} but got {moved_list}"

# Test 4: Multiple elements all not 0
list = [1, 1, 1, 1]
expected = [1, 1, 1, 1]
Solution().moveZeroes(list)
moved_list = list
assert moved_list == expected, f"Expected {expected} but got {moved_list}"

# Test 5: Multiple elements w/ 0
list = [0, 1, 0, 12, 15, 0]
expected = [1, 12, 15, 0, 0, 0]
Solution().moveZeroes(list)
moved_list = list
assert moved_list == expected, f"Expected {expected} but got {moved_list}"
