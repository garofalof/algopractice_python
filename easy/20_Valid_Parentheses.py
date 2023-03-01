class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        ops = {
            '(': ')',
            '[': ']',
            '{': '}',
        }
        for char in s:
            if char in ops:
                stack.append(ops[char])
            elif not stack or char != stack.pop():
                return False

        return not stack


"""
Explanation:

Initialize an empty stack to store opening parentheses, and a dictionary ops that maps opening parentheses to their corresponding closing parentheses. Then iterate over each character in the input string. If the current character is an opening parenthesis, its corresponding closing parenthesis is added to the stack list. If the current character is a closing parenthesis, the last item in the stack list is popped off the stack. If the popped value is not the expected closing parenthesis for the current character, or the stack list is empty when a closing parenthesis is encountered, return False. If the entire input string has been processed and there are no remaining opening parentheses in the stack, return True.

Notes:

Time complexity: O(n), as we iterate through each character in the input string exactly once.

Space complexity: O(n), as the size of the stack is directly proportional to the input string.
"""

# Test 1: Single open
s = '('
is_valid = Solution().isValid(s)
expected = False
assert is_valid == expected, f"Expected {expected} but got {is_valid}"

# Test 2: Single close
s = ')'
is_valid = Solution().isValid(s)
expected = False
assert is_valid == expected, f"Expected {expected} but got {is_valid}"

# Test 3: Valid, same character
s = '()'
is_valid = Solution().isValid(s)
expected = True
assert is_valid == expected, f"Expected {expected} but got {is_valid}"

# Test 4: Invalid, same character
s = '(('
is_valid = Solution().isValid(s)
expected = False
assert is_valid == expected, f"Expected {expected} but got {is_valid}"

# Test 5: Valid, multiple characters
s = '()[]{}'
is_valid = Solution().isValid(s)
expected = True
assert is_valid == expected, f"Expected {expected} but got {is_valid}"

# Test 6: Invalid, multiple characters
s = '([]{}'
is_valid = Solution().isValid(s)
expected = False
assert is_valid == expected, f"Expected {expected} but got {is_valid}"

# Test 7: Valid, multiple characters, nested
s = '([]){()}'
is_valid = Solution().isValid(s)
expected = True
assert is_valid == expected, f"Expected {expected} but got {is_valid}"

# Test 8: Invalid, multiple characters, nested
s = '([]{)}'
is_valid = Solution().isValid(s)
expected = False
assert is_valid == expected, f"Expected {expected} but got {is_valid}"
