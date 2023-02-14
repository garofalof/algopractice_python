class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0

        for char in columnTitle:
            result *= 26
            result += ord(char.lower()) - ord('a') + 1

        return result


"""
Explanation:

Initialize the result variable to 0. Iterate over each character in the columnTitle string. For each iteration, multiply the current result by 26 and add the 1-based integer value of the character. Finally, return the result variable after all characters have been processed.

Notes:

Time complexity: O(n)

Space complexity: O(1)
"""

# Test 1: Beginning of range
title = 'A'
number = Solution().titleToNumber(title)
assert number == 1, f"Expected 1 but got {number}"

# Test 2: End of range
title = 'FXSHRXW'
number = Solution().titleToNumber(title)
assert number == 2147483647, f"Expected 2147483647 but got {number}"