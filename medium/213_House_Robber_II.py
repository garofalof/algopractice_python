from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(start, end):
            prev, curr = 0, 0

            while start < end:
                prev, curr = curr, max(nums[start] + prev, curr)
                start += 1

            return curr

        first = helper(0, len(nums) - 1)
        second = helper(1, len(nums))

        return max(nums[0], first, second)

"""
Explanation:

Initialize helper function to find max robbed in array. Set previous max and current max robbed to 0. While start index < end, set previous max to current max, and update current max to max of current max or previous max plus current index and increase the start index. Once done, return the current max, which is the max robbed.

In the main function, call the helper function on the first n - 1 items, where n is the length of the input array and set it equal to first. Then call the helper on the 1 through n items in the array. By doing this, we ensure that the first and last houses are treated as non-adjacent.

Once done, get the max of the first element in the array, which accounts for only one house, the max of the first n - 1 items, or the max of items 1 through n.

Notes:

Time complexity: O(n), where n is the length of the input list

Space complexity: O(1)
"""

# Test Case 1: Increasing values
nums = [1, 2, 3, 4, 5]
result = Solution().rob(nums)
expected = 8
assert result == expected, f"Expected {expected} but got {result}"

# Test Case 2: Same start and end
nums = [5, 10, 5]
result = Solution().rob(nums)
expected = 10
assert result == expected, f"Expected {expected} but got {result}"

# Test Case 3: Random values
nums = [6, 2, 1, 8, 9, 3]
result = Solution().rob(nums)
expected = 16
assert result == expected, f"Expected {expected} but got {result}"

# Test Case 4: Single value
nums = [100]
result = Solution().rob(nums)
expected = 100
assert result == expected, f"Expected {expected} but got {result}"

# Test Case 5: Decreasing values
nums = [5, 4, 3, 2, 1]
result = Solution().rob(nums)
expected = 8
assert result == expected, f"Expected {expected} but got {result}"

# Test Case 6: All values 0
nums = [0, 0, 0, 0, 0]
result = Solution().rob(nums)
expected = 0
assert result == expected, f"Expected {expected} but got {result}"