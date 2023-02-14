class Solution:
    def decodeString(self, str):
        stack = []
        curr_str = ""
        curr_num = 0

        for char in str:
            if char == "[":
                stack.append(curr_str)
                stack.append(curr_num)

                curr_str, curr_num = "", 0
            elif char == "]":
                prev_num, prev_str = stack.pop(), stack.pop()
                curr_str = prev_str + curr_str * prev_num
            elif char.isdigit():
                curr_num = curr_num * 10 + int(char)
            else:
                curr_str += char

        return curr_str


"""
Explanation:

Initialize stack, curr_str, and curr_num variables. For each character in the input string: If it is "[", push curr_str and curr_num into the stack, reset curr_str to an empty string and curr_num to 0. If it is "]", pop the previous number and string from the stack, repeat the current string by the previous number, and concatenate the result with the previous string. If it is a digit, add it to the current number by multiplying curr_num by 10 and adding the integer value of the digit. If it is a letter, add it to the current string. Return curr_str after iterating through all characters in the input string.

Notes:

Time complexity: O(n)

Space complexity: O(n)
"""

# Test 1: Min length
str = 'a'
decoded = Solution().decodeString(str)
assert decoded == str, f"Expected {str} but got {decoded}"

# Test 2: Max length
str = 'a' * 30
decoded = Solution().decodeString(str)
assert decoded == str, f"Expected {str} but got {decoded}"

# Test 3: Min integer
str = '1[a]'
decoded = Solution().decodeString(str)
assert decoded == 'a', f"Expected 'a' but got {decoded}"

# Test 4: Max integer
str = '30[a]'
expected = 'a' * 30
decoded = Solution().decodeString(str)
assert decoded == expected, f"Expected {expected} but got {decoded}"

# Test 5: Multiple repetitions
str = '1[a]2[b]'
expected = 'abb'
decoded = Solution().decodeString(str)
assert decoded == expected, f"Expected {expected} but got {decoded}"

# Test 6: Nested repetitions
str = '3[a]2[a3[c]]'
expected = 'aaaacccaccc'
decoded = Solution().decodeString(str)
assert decoded == expected, f"Expected {expected} but got {decoded}"