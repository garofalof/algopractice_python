from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        l, m, r = 0, 0, len(nums) - 1

        while m <= r:
            if nums[m] == 0:
                nums[l], nums[m] = nums[m], nums[l]
                l += 1
                m += 1
            elif nums[m] == 2:
                nums[m], nums[r] = nums[r], nums[m]
                r -= 1
            else:
                m += 1


"""
Explanation:

Initialize left, mid, and right pointers to 0, 0, and len(nums) - 1. The left and right pointers keep track of the 0 and 2 boundaries, while the mid pointer is used to iterate through the array. While the mid pointer < the right pointer: if nums[mid] == 0, swap nums[mid] with nums[left] and increment both left and mid pointers by 1. If nums[mid] == 2, swap nums[mid] with nums[right] and decrement the right pointer by 1. If nums[mid] == 1, increment the mid pointer by 1. Once the algorithm finishes, the array will be sorted in-place such that all the 0s are on the left, followed by all the 1s, and then all the 2s.

Notes:

Time complexity: O(n), as we traverse the input array at most once

Space complexity: O(1), as we sort the array in place
"""

# Test Case 1: Already sorted array
nums = [0, 0, 1, 1, 2, 2]
Solution().sortColors(nums)
expected = [0, 0, 1, 1, 2, 2]
assert nums == expected, f"Expected {expected} but got {nums}"

# Test Case 2: Array with all 0s
nums = [0, 0, 0, 0, 0]
Solution().sortColors(nums)
expected = [0, 0, 0, 0, 0]
assert nums == expected, f"Expected {expected} but got {nums}"

# Test Case 3: Array with all 1s
nums = [1, 1, 1, 1, 1]
Solution().sortColors(nums)
expected = [1, 1, 1, 1, 1]
assert nums == expected, f"Expected {expected} but got {nums}"

# Test Case 4: Array with all 2s
nums = [2, 2, 2, 2, 2]
Solution().sortColors(nums)
expected = [2, 2, 2, 2, 2]
assert nums == expected, f"Expected {expected} but got {nums}"

# Test Case 5: Array with 0s, 1s, and 2s in random order
nums = [2, 0, 1, 2, 1, 0, 2, 1, 0]
Solution().sortColors(nums)
expected = [0, 0, 0, 1, 1, 1, 2, 2, 2]
assert nums == expected, f"Expected {expected} but got {nums}"
