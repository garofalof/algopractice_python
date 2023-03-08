from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n

        nums[:] = nums[::-1]
        nums[:k] = nums[:k][::-1]
        nums[k:] = nums[k:][::-1]


"""
Explanation:

First, compute the length of the list n. Then reduce the value of k to its equivalent in the range [0, n] by taking the modulo of k with n.

Next, reverse the entire list nums in place using Python's slice notation. This step puts the last k elements that will be rotated to the front of the list in their correct order, with the remaining elements also in their correct order.

To complete the rotation, reverse the first k elements of the list using the slice notation. This step puts the first k elements that will be rotated to the end of the list in their correct order.

Finally, reverse the remaining elements of the list using the slice notation. This step puts the remaining elements that were not reversed in the first step in their correct order.

Notes:

Time complexity: O(n), where n is the length of the input list nums.

Space complexity: O(1), as the input list is modified in place.
"""

# Test 1: Single element, k == 0
nums = [1]
k = 0
Solution().rotate(nums, k)
expected = [1]
assert nums == expected, f"Expected {expected} but got {nums}"

# Test 2: Single element, k == 1
nums = [1]
k = 1
Solution().rotate(nums, k)
expected = [1]
assert nums == expected, f"Expected {expected} but got {nums}"

# Test 3: Even number of elements, k == 0
nums = [1, 2, 3, 4]
k = 0
Solution().rotate(nums, k)
expected = [1, 2, 3, 4]
assert nums == expected, f"Expected {expected} but got {nums}"

# Test 4: Even number of elements, k == len(list)
nums = [1, 2, 3, 4]
k = len(nums)
Solution().rotate(nums, k)
expected = [1, 2, 3, 4]
assert nums == expected, f"Expected {expected} but got {nums}"

# Test 5: Even number of elements, k == middle
nums = [1, 2, 3, 4]
k = len(nums) // 2
Solution().rotate(nums, k)
expected = [3, 4, 1, 2]
assert nums == expected, f"Expected {expected} but got {nums}"

# Test 6: Odd number of elements, k == 0
nums = [1, 2, 3, 4, 5]
k = 0
Solution().rotate(nums, k)
expected = [1, 2, 3, 4, 5]
assert nums == expected, f"Expected {expected} but got {nums}"

# Test 7: Odd number of elements, k == len(list)
nums = [1, 2, 3, 4, 5]
k = len(nums)
Solution().rotate(nums, k)
expected = [1, 2, 3, 4, 5]
assert nums == expected, f"Expected {expected} but got {nums}"

# Test 8: Odd number of elements, k == middle
nums = [1, 2, 3, 4, 5]
k = len(nums) // 2
Solution().rotate(nums, k)
expected = [4, 5, 1, 2, 3]
assert nums == expected, f"Expected {expected} but got {nums}"
