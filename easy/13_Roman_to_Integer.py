class Solution:
    def romanToInt(self, s: str) -> int:
        romans = "IVXLCDM"
        nums = [1, 5, 10, 50, 100, 500, 1000]
        map = {romans[i]: nums[i] for i in range(len(romans))}
        result = 0

        for i in range(len(s)):
            curr = map[s[i]]
            next = map[s[i + 1]] if i + 1 < len(s) else 0

            result += -curr if curr < next else curr

        return result

"""
Explanation:

First, initialize the romans string with the Roman numerals and the nums list with their corresponding integer values. Then create a mapping between the Roman numerals and integers. Next, loop through the characters of the input string s. At each iteration, retrieve the current and next characters' integer values from the mapping dictionary. If the current value < next value, subtract the current value from the result; otherwise, add the current value to the result. Finally, return the result integer value.

Notes:

Time complexity: O(n)

Space complexity: O(1)
"""

# Test Case 1: s == 'III'
s = 'III'
result = Solution().romanToInt(s)
expected = 3
assert result == expected, f"Expected {expected} but got {result}"

# Test Case 2: s == 'IV'
s = 'IV'
result = Solution().romanToInt(s)
expected = 4
assert result == expected, f"Expected {expected} but got {result}"

# Test Case 3: s == 'IX'
s = 'IX'
result = Solution().romanToInt(s)
expected = 9
assert result == expected, f"Expected {expected} but got {result}"

# Test Case 4: s == 'LVIII'
s = 'LVIII'
result = Solution().romanToInt(s)
expected = 58
assert result == expected, f"Expected {expected} but got {result}"

# Test Case 5: s == 'MCMXCIV'
s = 'MCMXCIV'
result = Solution().romanToInt(s)
expected = 1994
assert result == expected, f"Expected {expected} but got {result}"