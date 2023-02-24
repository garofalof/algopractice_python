from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        count = left = right = 0

        for i, num in enumerate(nums[:-1]):
            right = max(right, i + num)

            if i == left:
                count += 1
                left = right

        return count


"""
Explanation:

Initialize variables count, left, and right to 0. Iterate through the list nums using the enumerate() function, except for the last element of the list. For each element, update the right variable to be the maximum value between right and the sum of the index i and the value num.
Then check if i is equal to left. If so, increment the count variable and set left == right. This we have found the furthest index we can jump to from the current range, and we need to make another jump to the next range. Once done, return the count variable.

Notes:

Time complexity: O(n), as we iterate through the input list exactly once.

Space complexity: O(1)
"""

# Test 1: Single element
nums = [1]
min_jump = Solution().jump(nums)
expected = 0
assert min_jump == expected, f"Expected {expected} but got {min_jump}"

# Test 2: All elements same
nums = [1, 1, 1, 1]
min_jump = Solution().jump(nums)
expected = 3
assert min_jump == expected, f"Expected {expected} but got {min_jump}"

# Test 3: All elements increasing
nums = [1, 2, 3, 4]
min_jump = Solution().jump(nums)
expected = 2
assert min_jump == expected, f"Expected {expected} but got {min_jump}"

# Test 4: All elements decreasing
nums = [4, 3, 2, 1]
min_jump = Solution().jump(nums)
expected = 1
assert min_jump == expected, f"Expected {expected} but got {min_jump}"

# Test 5: Some elements zero
nums = [2, 0, 1, 3, 0, 4, 0, 0]
min_jump = Solution().jump(nums)
expected = 4
assert min_jump == expected, f"Expected {expected} but got {min_jump}"

# Test 6: Mixed large and small elements
nums = [2, 10, 4, 2, 7, 3, 5, 1]
min_jump = Solution().jump(nums)
expected = 2
assert min_jump == expected, f"Expected {expected} but got {min_jump}"
