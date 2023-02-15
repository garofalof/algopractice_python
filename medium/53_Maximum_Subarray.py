from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        maxEnd = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]
            maxEnd = max(maxEnd + num, num)
            maxSum = max(maxSum, maxEnd)

        return maxSum

"""
Explanation:

Initialize two variables, maxSum and maxEnd, to the first element of nums, and iterate through the rest of the list. For each element nums, update maxEnd to the max of either adding num to the sum ending at the previous element or just taking num alone. Then update maxSum to the max of its current value and maxEnd, since we have found a new max subarray sum.

At the end of the loop, return maxSum.

Notes:

Time complexity: O(n), where n is the length of the input list nums, since we iterate through the list once.

Space complexity: O(1), since we use constant extra space to store the variables maxSum and maxEnd.
"""

# Test 1: Single element in list
nums = [1]
max_sum = Solution().maxSubArray(nums)
expected = 1
assert max_sum == expected, f"Expected {expected} but got {max_sum}"

# Test 2: All negatives increasing
nums = [-4, -3, -2, -1]
max_sum = Solution().maxSubArray(nums)
expected = -1
assert max_sum == expected, f"Expected {expected} but got {max_sum}"

# Test 3: All negatives decreasing
nums = [-1, -2, -3, -4]
max_sum = Solution().maxSubArray(nums)
expected = -1
assert max_sum == expected, f"Expected {expected} but got {max_sum}"

# Test 4: All positives increasing
nums = [1, 2, 3, 4]
max_sum = Solution().maxSubArray(nums)
expected = 10
assert max_sum == expected, f"Expected {expected} but got {max_sum}"

# Test 5: All positives decreasing
nums = [4, 3, 2, 1]
max_sum = Solution().maxSubArray(nums)
expected = 10
assert max_sum == expected, f"Expected {expected} but got {max_sum}"

# Test 6: Mixed integers
nums = [-1, 2, -4, 5, 3, -1]
max_sum = Solution().maxSubArray(nums)
expected = 8
assert max_sum == expected, f"Expected {expected} but got {max_sum}"