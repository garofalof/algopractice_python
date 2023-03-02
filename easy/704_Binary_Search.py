from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (r - l) // 2 + l

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        return -1


"""
Explanation:

Start with two pointers, l and r, representing the leftmost and rightmost indices of the list, respectively. Then, calculate the midpoint of the list by taking the average of l and r. If the value at the midpoint == the target, return the index of the midpoint. If the value at the midpoint < the target, set l to the midpoint + 1 to search the right half of the list. Otherwise, set r to the midpoint - 1 to search the left half of the list. Repeat this process until the target is found or the search space is exhausted.

Notes:

Time complexity: O(log n), where n is the length of the input list. This is because the search space is halved with each iteration of the algorithm.

Space complexity: O(1), as we use constant space to store pointers.
"""

# Test 1: Single element, target in list
nums = [1]
target = 1
found_index = Solution().search(nums, target)
expected = 0
assert found_index == expected, f"Expected {expected} but got {found_index}"

# Test 2: Single element, target not in list
nums = [1]
target = 5
found_index = Solution().search(nums, target)
expected = -1
assert found_index == expected, f"Expected {expected} but got {found_index}"

# Test 3: Target in middle
nums = [0, 1, 3, 5, 7, 12, 15]
target = 5
found_index = Solution().search(nums, target)
expected = 3
assert found_index == expected, f"Expected {expected} but got {found_index}"

# Test 4: Target at beginning
nums = [0, 1, 3, 5, 7, 12, 15]
target = 0
found_index = Solution().search(nums, target)
expected = 0
assert found_index == expected, f"Expected {expected} but got {found_index}"

# Test 5: Target at end
nums = [0, 1, 3, 5, 7, 12, 15]
target = 15
found_index = Solution().search(nums, target)
expected = len(nums) - 1
assert found_index == expected, f"Expected {expected} but got {found_index}"

# Test 6: Target not in list
nums = [0, 1, 3, 5, 7, 12, 15]
target = 27
found_index = Solution().search(nums, target)
expected = -1
assert found_index == expected, f"Expected {expected} but got {found_index}"
