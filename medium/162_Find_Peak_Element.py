from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            mid = (r - l) // 2 + l

            if nums[mid] > nums[mid + 1]:
                r = mid
            else:
                l = mid + 1

        return l


"""
Explanation:

Initialize pointers l and r to the start and end of the list. Then, continue to update the middle pointer until the left pointer >= right pointer. At each iteration, if the middle element > next element, the right pointer is updated to the middle index. Otherwise, the left pointer is updated to the middle index + 1. Finally, return the left pointer, which should correspond to the index of the peak element.

Notes:

Time complexity: O(log n), as we use binary search to find the peak element.

Space complexity: O(1), as we use constant extra space to store the pointers.
"""

# Test 1: Single element
nums = [1]
peak = Solution().findPeakElement(nums)
expected = 0
assert peak == expected, f"Expected {expected} but got {peak}"

# Test 2: Two elements, decreasing
nums = [2, 1]
peak = Solution().findPeakElement(nums)
expected = 0
assert peak == expected, f"Expected {expected} but got {peak}"

# Test 3: Two elements, increasing
nums = [2, 1]
peak = Solution().findPeakElement(nums)
expected = 0
assert peak == expected, f"Expected {expected} but got {peak}"

# Test 4: Peak at beginning
nums = [7, 5, 3, 2, 1]
peak = Solution().findPeakElement(nums)
expected = 0
assert peak == expected, f"Expected {expected} but got {peak}"

# Test 5: Peak at end
nums = [1, 2, 5, 6, 8]
peak = Solution().findPeakElement(nums)
expected = 4
assert peak == expected, f"Expected {expected} but got {peak}"

# Test 6: Peak in middle
nums = [1, 2, 8, 6, 5]
peak = Solution().findPeakElement(nums)
expected = 2
assert peak == expected, f"Expected {expected} but got {peak}"

# Test 6: All elements same
nums = [4, 4, 4, 4]
peak = Solution().findPeakElement(nums)
expected = (0, 1, 2, 3)
assert peak in expected, f"Expected {expected} but got {peak}"
