class Solution:
    def checkValidString(self, s: str) -> bool:
        left_max, left_min = 0, 0

        for char in s:
            if char == '(':
                left_min += 1
                left_max += 1
            elif char == ')':
                left_min -= 1
                left_max -= 1
            else:
                left_min -= 1
                left_max += 1
            if left_max < 0:
                return False
            if left_min < 0:
                left_min = 0

        return left_min == 0


"""
Explanation:

Keep track of the min and max number of open parentheses left_min and left_max that could be represented by the string so far. If left_max becomes negative at any point, it means there are too many closing parentheses in the remaining portion of the string to be balanced by the open parentheses, so the string is invalid. If left_min becomes negative, it means there are too many asterisks being used as closing parentheses, so they must be counted as open parentheses instead.

Finally, return True if left_min is zero, indicating that all parentheses have been balanced, and False otherwise.

Notes:

Time complexity: O(n), where n is the length of the input string.

Space complexity: O(1), as we use constant extra space to store the left_max and left_min pointers.
"""

# Test 1: No parentheses
s = '*'
is_valid = Solution().checkValidString(s)
expected = True
assert is_valid == expected, f"Expected {expected} but got {is_valid}"

# Test 2: Open parentheses
s = '('
is_valid = Solution().checkValidString(s)
expected = False
assert is_valid == expected, f"Expected {expected} but got {is_valid}"

# Test 3: Open parentheses
s = ')'
is_valid = Solution().checkValidString(s)
expected = False
assert is_valid == expected, f"Expected {expected} but got {is_valid}"

# Test 4: Balanced
s = '()'
is_valid = Solution().checkValidString(s)
expected = True
assert is_valid == expected, f"Expected {expected} but got {is_valid}"

# Test 5: Open > close parentheses
s = '(((*))'
is_valid = Solution().checkValidString(s)
expected = True
assert is_valid == expected, f"Expected {expected} but got {is_valid}"

# Test 6: Open < close parentheses
s = '((())))'
is_valid = Solution().checkValidString(s)
expected = False
assert is_valid == expected, f"Expected {expected} but got {is_valid}"

# Test 7: All asterisks
s = '****'
is_valid = Solution().checkValidString(s)
expected = True
assert is_valid == expected, f"Expected {expected} but got {is_valid}"
