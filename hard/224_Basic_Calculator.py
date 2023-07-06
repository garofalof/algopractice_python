class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        sign, num = 1, 0
        result = 0

        for i in range(len(s)):
            if s[i].isdigit():
                num = num * 10 + int(s[i])
            if s[i] in ('-', '+'):
                result += sign * num
                num = 0
                sign = 1 if s[i] == '+' else -1
            if s[i] == '(':
                stack.append(result)
                stack.append(sign)

                result, sign = 0, 1
            if s[i] == ')':
                result += sign * num
                num = 0
                result *= stack.pop()
                result += stack.pop()

        return result + sign * num

"""
Explanation:

The code iterates through the given string `s` character by character, performing the necessary operations to calculate the result. A list `stack` is used to store previous results and signs encountered when encountering parentheses. A variable `sign` keeps track of the current sign. A variable `num` stores the current number being built from consecutive digits encountered. A variable `result` holds the cumulative result of the arithmetic expression.

For each character in the input string s: if the character is a digit, it appends it to the current number being built by multiplying it by 10 and adding the integer value of the character. If the character is '+' or '-', it adds the current num multiplied by the sign to the result, resets num to 0, and updates the sign accordingly. If the character is '(', it stores the current result and sign in the stack, resets result to 0, and sets the sign to 1. If the character is ')', it adds the current num multiplied by the sign to the result, resets num to 0, multiplies the result by the previous sign popped from the stack, and adds the previous result popped from the stack to the current result. Once done, we return the final result.

Notes:

Time complexity: O(n), where n is the number of characters in input string `s`

Space complexity: O(m), where m is the number of nested parentheses, as we push up to the stack every time we encounter a parentheses
"""

# Test Case 1: Basic addition
s = "1 + 3"
result = Solution().calculate(s)
expected = 4
assert result == expected, f"Expected {expected} but got {result}"

# Test Case 2: Basic subtraction
s = "4 - 1"
result = Solution().calculate(s)
expected = 3
assert result == expected, f"Expected {expected} but got {result}"

# Test Case 3: Parentheses
s = "(1 + 3) + 3"
result = Solution().calculate(s)
expected = 7
assert result == expected, f"Expected {expected} but got {result}"

# Test Case 4: Nested parentheses
s = "(1 + (1 - 2)) + 3"
result = Solution().calculate(s)
expected = 3
assert result == expected, f"Expected {expected} but got {result}"

# Test Case 5: Single number
s = "42"
result = Solution().calculate(s)
expected = 42
assert result == expected, f"Expected {expected} but got {result}"

# Test Case 6: Empty string
s = " "
result = Solution().calculate(s)
expected = 0
assert result == expected, f"Expected {expected} but got {result}"