from typing import List


class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        total = 0

        for i in range(len(nums)):
            smaller = larger = nums[i]

            for j in range(i + 1, len(nums)):
                smaller = min(smaller, nums[j])
                larger = max(larger, nums[j])

                total += larger - smaller

        return total


"""
Explanation:

Iterate over all possible start points i of a subarray. For each i, then iterates over all possible end points j of the subarray that starts at i + 1. For each pair of indices (i, j), calculate the smallest and largest elements of the subarray, smaller and larger, respectively. Then add the difference between larger and smaller to the running total. Once done iterating over all subarray ranges, return the total count of subarrays whose elements are in non-descending order.

Notes:

Time complexity: O(n ^ 2), as iterate over the input array at each index in the array.

Space complexity: O(1), as we use constant extra space to store the variables total, smaller, and larger.
"""

# Test 1: Random positive values
nums = [3, 1, 2, 4]
subarray_sum = Solution().subArrayRanges(nums)
expected = 13
assert subarray_sum == expected, f"Expected {expected} but got {subarray_sum}"

# Test 2: Random negative values
nums = [-2, -3, -4, -1, -2, -1, -5, -3]
subarray_sum = Solution().subArrayRanges(nums)
expected = 84
assert subarray_sum == expected, f"Expected {expected} but got {subarray_sum}"

# Test 3: Same values
nums = [5] * 5
subarray_sum = Solution().subArrayRanges(nums)
expected = 0
assert subarray_sum == expected, f"Expected {expected} but got {subarray_sum}"

# Test 4: Single value
nums = [1]
subarray_sum = Solution().subArrayRanges(nums)
expected = 0
assert subarray_sum == expected, f"Expected {expected} but got {subarray_sum}"
