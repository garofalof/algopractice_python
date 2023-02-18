from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        prev_max, curr_max = 0, 0

        for num in nums:
            prev_max, curr_max = curr_max, max(curr_max, prev_max + num)

        return curr_max

"""
Explanation:

Initialize variables "prev_max" and "curr_max" to keep track of previous and current maximum robbed value. For each house, set prev_max to curr_max and set curr_max to the greater of the max value robbed at the previous house or the max value robbed two houses ago plus the value robbed at the current house. Once done, return curr_max to get the max value we can rob.

Notes:

Time complexity: O(n), where n is the length of the input array.

Space complexity: O(1)
"""

# Test 1: Single value == 0
nums = [0]
max_value = Solution().rob(nums)
expected = 0
assert max_value == expected, f"Expected {expected} but got {max_value}"

# Test 2: Single value == 400
nums = [400]
max_value = Solution().rob(nums)
expected = 400
assert max_value == expected, f"Expected {expected} but got {max_value}"

# Test 3: Odd number of values, increasing
nums = [1, 2, 3]
max_value = Solution().rob(nums)
expected = 4
assert max_value == expected, f"Expected {expected} but got {max_value}"

# Test 4: Odd number of values, decreasing
nums = [3, 2, 1]
max_value = Solution().rob(nums)
expected = 4
assert max_value == expected, f"Expected {expected} but got {max_value}"

# Test 5: Odd number of values, mixed
nums = [2, 1, 3]
max_value = Solution().rob(nums)
expected = 5
assert max_value == expected, f"Expected {expected} but got {max_value}"

# Test 6: Even number of values, increasing
nums = [1, 2, 3, 4]
max_value = Solution().rob(nums)
expected = 6
assert max_value == expected, f"Expected {expected} but got {max_value}"

# Test 7: Even number of values, decreasing
nums = [4, 3, 2, 1]
max_value = Solution().rob(nums)
expected = 6
assert max_value == expected, f"Expected {expected} but got {max_value}"

# Test 8: Even number of values, mixed
nums = [1, 4, 3, 2]
max_value = Solution().rob(nums)
expected = 6
assert max_value == expected, f"Expected {expected} but got {max_value}"
