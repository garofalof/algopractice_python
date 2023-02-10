class Solution:
    def calculate(self, s: str) -> int:
        if s is None or len(s) == 0:
            return 0

        stack = []
        num = 0
        operator = '+'

        operations = {
            '+': lambda x: x,
            '-': lambda x: -x,
            '*': lambda x, y: x * y,
            '/': lambda x, y: int(x / y),
        }

        for i in range(len(s)):
            token = s[i]

            if token.isdigit():
                num = num * 10 + int(token)
            if token in operations or i == len(s) - 1:
                if operator == '*' or operator == '/':
                    stack.append(operations[operator](stack.pop(), num))
                else:
                    stack.append(operations[operator](num))

                operator = token
                num = 0

        return sum(stack)


"""
Explanation:

Create a stack to store intermediate results. Track the current number being processed and the current operator. Use a map to store the operations as functions. Iterate over the input string and perform the following actions: if the current character is a digit, add it to the current number being processed. If the current character is an operator or if it's the last character in the string, perform the appropriate operation and update the stack, the current operator, and reset the current number. Finally, return the sum of the values in the stack.

Notes:

Time Complexity: O(n)
Space Complexity: O(n)
"""

# Test case 1
s = "3 + 2 * 2"
result = Solution().calculate(s)
assert result == 7, f"Expected 7 but got {result}"

# Test case 2
s = "3/2"
result = Solution().calculate(s)
assert result == 1, f"Expected 1 but got {result}"

# Test case 3
s = " 3+5 / 2 "
result = Solution().calculate(s)
assert result == 5, f"Expected 5 but got {result}"

# Test case 4
s = "0"
result = Solution().calculate(s)
assert result == 0, f"Expected 0 but got {result}"

# Test case 5
s = "1000000000+1000000000"
result = Solution().calculate(s)
assert result == 2000000000, f"Expected 2000000000 but got {result}"

# Test case 6
s = "1000000000-1000000000"
result = Solution().calculate(s)
assert result == 0, f"Expected 0 but got {result}"

# Test case 7
s = "2147483647 + 1"
result = Solution().calculate(s)
assert result == 2147483648, f"Expected 2147483648 but got {result}"

# Test case 8
s = "2147483647 - 2"
result = Solution().calculate(s)
assert result == 2147483645, f"Expected 2147483645 but got {result}"
