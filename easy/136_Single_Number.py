import random
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        unique = 0

        for num in nums:
            unique ^= num

        return unique


"""
Explanation:

Set the 'unique' variable to 0. Then iterate over the list and XOR each element of the list with the 'unique' variable. This has the effect of toggling the bits of the 'unique' variable for each corresponding bit that is toggled in the input element.

Since the XOR operator is associative and commutative, the end result is that all elements that appear twice in the input list will cancel each other out, leaving only the unique element XOR'd with 0. Thus, the final value of 'unique' is the unique element in the list.

Notes:

Time Complexity: O(n), as we iterate through the entire input list.

Space Complexity: O(1), as we use constant space to store the 'unique' variable.
"""

# Test 1: Single number, min value
min_value = -3 * 10 ** 4
nums = [min_value]
unique = Solution().singleNumber(nums)
expected = min_value
assert unique == expected, f"Expected {expected} but got {unique}"

# Test 2: Single number, max value
max_value = 3 * 10 ** 4
nums = [max_value]
unique = Solution().singleNumber(nums)
expected = max_value
assert unique == expected, f"Expected {expected} but got {unique}"

# Test 3: Max length, random missing
n = 3 * 10 ** 4
rand = random.randint(0, n - 1)
nums = [i for i in range(n) if i != rand] * 2 + [rand]
unique = Solution().singleNumber(nums)
expected = rand
assert unique == expected, f"Expected {expected} but got {unique}"

# Test 4: Missing number beginning
nums = [1, 2, 2, 4, 4, 3, 3]
unique = Solution().singleNumber(nums)
expected = 1
assert unique == expected, f"Expected {expected} but got {unique}"

# Test 5: Missing number end
nums = [1, 1, 4, 4, 3, 3, 2]
unique = Solution().singleNumber(nums)
expected = 2
assert unique == expected, f"Expected {expected} but got {unique}"

# Test 6: Missing number, mixed list
nums = [1, 4, 1, 2, 3, 2, 3]
unique = Solution().singleNumber(nums)
expected = 4
assert unique == expected, f"Expected {expected} but got {unique}"
