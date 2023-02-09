from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in reversed(range(len(digits))):
            if digits[i] != 9:
                digits[i] += 1
                return digits

            digits[i] = 0

        digits = [1] + digits

        return digits


"""
Explanation:

Iterate over the digits list in reverse order. For each digit, check if it's not 9. If it's not, add 1 to the digit and return the digits list. If the digit is 9, set it to 0 and continue with the next digit. If all the digits were 9, add a 1 to the beginning of the digits list and return it.

Notes:

Time complexity: O(n)
Space complexity: O(1)
"""

# Test case 1: Single digit not 9
digits = [1]
result = Solution().plusOne(digits)
assert result == [2], f"Expected [2] but got {result}"

# Test case 2: Single digit is 9
digits = [9]
result = Solution().plusOne(digits)
assert result == [1, 0], f"Expected [1, 0] but got {result}"

# Test case 3: Multiple digits not ending in 9
digits = [4, 2, 1]
result = Solution().plusOne(digits)
assert result == [4, 2, 2], f"Expected [4, 2, 2] but got {result}"

# Test case 4: Multiple digits ending in 9
digits = [9, 9, 9]
result = Solution().plusOne(digits)
assert result == [1, 0, 0, 0], f"Expected [1, 0, 0, 0] but got {result}"
