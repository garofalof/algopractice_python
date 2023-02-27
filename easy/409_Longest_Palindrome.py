from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq = Counter(s)
        count = sum(freq[char] // 2 * 2 for char in freq)

        return count + 1 if count < len(s) else count


"""
Explanation:

Create a Counter object freq to count the frequency of each character in the string. Initialize a variable count to the sum of the even counts of each character in freq. To do this, use a generator expression that iterates over the keys in freq, calculates the integer division of the count of each character by 2, and multiplies it by 2. This ensures that we only add even counts to the sum.

Next, we check if the length of s < count + 1. If so, we return count, since we can use all of the even-counted characters to form a palindrome. Otherwise, we return count + 1, since we can use all of the even-counted characters, plus one odd-counted character as the center of the palindrome.

Notes:

Time complexity: O(n), as we use the Counter object to count the character frequencies in the input string.

Space complexity: O(1), as we store max 26 characters in the Counter object.
"""

# Test 1: Single character
s = 'a'
longest_pal = Solution().longestPalindrome(s)
expected = 1
assert longest_pal == expected, f"Expected {expected} but got {longest_pal}"

# Test 2: All lowercase, all even frequencies
s = 'aabbcc'
longest_pal = Solution().longestPalindrome(s)
expected = 6
assert longest_pal == expected, f"Expected {expected} but got {longest_pal}"

# Test 3: All uppercase, all even frequencies
s = 'AABBCC'
longest_pal = Solution().longestPalindrome(s)
expected = 6
assert longest_pal == expected, f"Expected {expected} but got {longest_pal}"

# Test 4: Mixed characters, all even frequencies
s = 'aaAAbbBBccCC'
longest_pal = Solution().longestPalindrome(s)
expected = 12
assert longest_pal == expected, f"Expected {expected} but got {longest_pal}"

# Test 5: All lowercase, all odd frequencies
s = 'aaabccc'
longest_pal = Solution().longestPalindrome(s)
expected = 5
assert longest_pal == expected, f"Expected {expected} but got {longest_pal}"

# Test 6: All uppercase, all odd frequencies
s = 'AAABCCC'
longest_pal = Solution().longestPalindrome(s)
expected = 5
assert longest_pal == expected, f"Expected {expected} but got {longest_pal}"

# Test 7: Mixed characters, all odd frequencies
s = 'aAbbbBccc'
longest_pal = Solution().longestPalindrome(s)
expected = 5
assert longest_pal == expected, f"Expected {expected} but got {longest_pal}"

# Test 8: Mixed characters, mixed frequencies
s = 'aaBbbCcccc'
longest_pal = Solution().longestPalindrome(s)
expected = 9
assert longest_pal == expected, f"Expected {expected} but got {longest_pal}"
