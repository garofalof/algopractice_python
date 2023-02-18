class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(c.lower() for c in s if c.isalnum())

        return s == s[::-1]

"""
Explanation:

Use list comprehension to join create a string "s" that consists of only lowercase alphanumeric characters. Then, check whether "s" is equal to its reverse and return that value.

Notes:

Time complexity: O(n), where n is the length of the input string.

Space complexity: O(n), as we store all alphanumeric characters in the new string "s".
"""

# Test 1: Single character, non alphanumeric
s = ' '
is_palindrome = Solution().isPalindrome(s)
expected = True
assert is_palindrome == expected, f"Expected {expected} but got {is_palindrome}"

# Test 2: Single character, alphanumeric
s = 'a'
is_palindrome = Solution().isPalindrome(s)
expected = True
assert is_palindrome == expected, f"Expected {expected} but got {is_palindrome}"

# Test 3: Palindrome w/ only alphanumeric
s = 'abba'
is_palindrome = Solution().isPalindrome(s)
expected = True
assert is_palindrome == expected, f"Expected {expected} but got {is_palindrome}"

# Test 4: Nonpalindrome w/ only alphanumeric
s = 'abc'
is_palindrome = Solution().isPalindrome(s)
expected = False
assert is_palindrome == expected, f"Expected {expected} but got {is_palindrome}"

# Test 5: Palindrome w/ mix of characters
s = 'reed, deer'
is_palindrome = Solution().isPalindrome(s)
expected = True
assert is_palindrome == expected, f"Expected {expected} but got {is_palindrome}"

# Test 6: Nonpalindrome w/ mix of characters
s = 'hello, world'
is_palindrome = Solution().isPalindrome(s)
expected = False
assert is_palindrome == expected, f"Expected {expected} but got {is_palindrome}"

