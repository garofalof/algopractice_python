from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            mid = (r - l) // 2 + l

            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid

        return nums[l]


"""
Explanation:

Initialize variables l and r to the first and last indices of the input array. In each iteration of the while loop, calculate the mid index. If the value at mid index is greater than the value at the last index, update the left pointer to mid + 1, because the min value cannot be present in the left half. Otherwise, update the right pointer to mid, because the min value cannot be present in the right half. The loop continues until l becomes equal to r, which means that we have found the index of the min element. Finally, return the value at this index in the array.

Notes:

Time complexity: O(log n), as we implement a binary search algorithm to find the min element in the input array.

Space complexity: O(1), as we use constant extra space to store the left, right, and mid pointers.
"""

# Test 1: Single element
n = [1]
min = Solution().findMin(n)
expected = 1
assert min == expected, f"Expected {expected} but got {min}"

# Test 2: Array not rotated
n = [1, 2, 3, 4, 5]
min = Solution().findMin(n)
expected = 1
assert min == expected, f"Expected {expected} but got {min}"

# Test 3: Multiple rotations
n = [7, 8, 1, 2, 3, 4, 5, 6]
min = Solution().findMin(n)
expected = 1
assert min == expected, f"Expected {expected} but got {min}"

# Test 4: Negative numbers in array, not rotated
n = [-5, -3, 1, 3, 5]
min = Solution().findMin(n)
expected = -5
assert min == expected, f"Expected {expected} but got {min}"

# Test 5: Negative numbers in array, rotated
n = [-4, -2, 1, 3, -5]
min = Solution().findMin(n)
expected = -5
assert min == expected, f"Expected {expected} but got {min}"
