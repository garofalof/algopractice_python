from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first_num = second_num = float('inf')

        for num in nums:
            if num <= first_num:
                first_num = num
            elif num <= second_num:
                second_num = num
            else:
                return True

        return False


"""
Explanation:

Initialize two variables 'first_num' and 'second_num' to positive infinity. Iterate through each number in the list. If the current number <= the value of 'first_num', set 'first_num' to the current number. Else, if the current number <= the value of 'second_num', set 'second_num' to the current number. Else, the current number > both 'first_num' and 'second_num', so there exists an increasing subsequence of length 3, so return True.

If the loop completes without finding an increasing subsequence of length 3, return False.

Notes:

Time complexity: O(n), where n is the length of the input list.

Space complexity: O(1), as the function uses only a constant amount of extra space.
"""

# Test 1: Single number
nums = [1]
has_triplet = Solution().increasingTriplet(nums)
expected = False
assert has_triplet == expected, f"Expected {expected} but got {has_triplet}"

# Test 2: Two numbers
nums = [1, 2]
has_triplet = Solution().increasingTriplet(nums)
expected = False
assert has_triplet == expected, f"Expected {expected} but got {has_triplet}"

# Test 3: Three numbers, true
nums = [1, 2, 3]
has_triplet = Solution().increasingTriplet(nums)
expected = True
assert has_triplet == expected, f"Expected {expected} but got {has_triplet}"

# Test 4: Three numbers, false
nums = [2, 1, 3]
has_triplet = Solution().increasingTriplet(nums)
expected = False
assert has_triplet == expected, f"Expected {expected} but got {has_triplet}"

# Test 5: > 3, increasing
nums = [1, 2, 3, 4, 5]
has_triplet = Solution().increasingTriplet(nums)
expected = True
assert has_triplet == expected, f"Expected {expected} but got {has_triplet}"

# Test 6: > 3, decreasing
nums = [5, 4, 3, 2, 1]
has_triplet = Solution().increasingTriplet(nums)
expected = False
assert has_triplet == expected, f"Expected {expected} but got {has_triplet}"

# Test 6: > 3, mixed
nums = [2, 1, 7, 3, 0, 5]
has_triplet = Solution().increasingTriplet(nums)
expected = True
assert has_triplet == expected, f"Expected {expected} but got {has_triplet}"
