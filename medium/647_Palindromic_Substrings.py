class Solution:
    def countSubstrings(self, s: str) -> int:
        def countPalindromes(l: int, r: int) -> int:
            count = 0

            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1

            return count

        count = 0

        for i in range(len(s)):
            count += countPalindromes(i, i)
            count += countPalindromes(i, i + 1)

        return count


"""
Explanation:

Iterate through every index in the string, and then for each index, create two "center points" around which to check for palindromic substrings. The two center points correspond to two scenarios: one where the center of the palindrome is a single character, and one where the center is two characters. To check for palindromic substrings, expand outward from each center point, checking that the characters on either side are equal. If a palindromic substring is found, increment the count by 1. Return the total count of palindromic substrings found.

Notes:

Time complexity: O(n^2), where n is the length of the input string. This is because the function needs to iterate over every index in the string and check around each index for palindromic substrings.

Space complexity: O(1), as the function only uses a constant amount of additional memory.
"""

# Test 1: Single character
input_str = 'a'
palindrome_count = Solution().countSubstrings(input_str)
expected = 1
assert palindrome_count == expected, f"Expected {expected} but got {palindrome_count}"

# Test 2: Even characters unique
input_str = 'abcd'
palindrome_count = Solution().countSubstrings(input_str)
expected = 4
assert palindrome_count == expected, f"Expected {expected} but got {palindrome_count}"

# Test 3: Even characters duplicates
input_str = 'aabccd'
palindrome_count = Solution().countSubstrings(input_str)
expected = 8
assert palindrome_count == expected, f"Expected {expected} but got {palindrome_count}"

# Test 4: Odd characters unique
input_str = 'abc'
palindrome_count = Solution().countSubstrings(input_str)
expected = 3
assert palindrome_count == expected, f"Expected {expected} but got {palindrome_count}"

# Test 5: Odd characters w/ palindrome
input_str = 'aabcc'
palindrome_count = Solution().countSubstrings(input_str)
expected = 7
assert palindrome_count == expected, f"Expected {expected} but got {palindrome_count}"
