from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            total = numbers[l] + numbers[r]

            if total == target:
                return [l + 1, r + 1]
            elif total < target:
                l += 1
            else:
                r -= 1

        return []


"""
Explanation:

Initialize pointers l and r to the start and end of the list. Enter a loop to calculate the sum of the numbers at indices l and r. If total == target, return a list containing the indices of the two numbers. If total < target, move the left pointer l to the right. If total > target, move the right pointer r to the left. If the loop exits without finding a match, an empty list is returned.

Notes:

Time complexity: O(n), as the input array is traversed at most once.

Space complexity: O(1), as we use constant extra space to store the two pointers and sum.
"""

# Test 1: Min length, not valid
nums = [2, 4]
target = 7
two_sum = Solution().twoSum(nums, target)
expected = []
assert two_sum == expected, f"Expected {expected} but got {two_sum}"

# Test 2: Min length, valid
nums = [2, 4]
target = 6
two_sum = Solution().twoSum(nums, target)
expected = [1, 2]
assert two_sum == expected, f"Expected {expected} but got {two_sum}"

# Test 3: Valid pair
nums = [2, 7, 11, 15]
target = 9
two_sum = Solution().twoSum(nums, target)
expected = [1, 2]
assert two_sum == expected, f"Expected {expected} but got {two_sum}"

# Test 4: No valid pair
nums = [2, 7, 11, 15]
target = 14
two_sum = Solution().twoSum(nums, target)
expected = []
assert two_sum == expected, f"Expected {expected} but got {two_sum}"

# Test 5: Duplicate valid pair
nums = [3, 3, 4]
target = 6
two_sum = Solution().twoSum(nums, target)
expected = [1, 2]
assert two_sum == expected, f"Expected {expected} but got {two_sum}"

# Test 6: Duplicate invalid pair
nums = [3, 2, 5]
target = 6
two_sum = Solution().twoSum(nums, target)
expected = []
assert two_sum == expected, f"Expected {expected} but got {two_sum}"
