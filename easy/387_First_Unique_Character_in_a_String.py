from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = Counter(s)

        for i, c in enumerate(s):
           if count[c] == 1:
               return i

        return -1


"""
Explanation:

Use a counter to initialize a dictionary "count" that stores the frequency of each character in the input string. For each character in the input string, check if the character's frequency is 1 and, if so, return its index. If we iterate through the entire string without finding a unique character, return -1.

Notes:

Time complexity: O(n), where n is the length of the string.

Space complexity: O(1), as we store max 26 characters.
"""

# Test 1: Single character
s = 'a'
first_unique = Solution().firstUniqChar(s)
expected = 0
assert first_unique == expected, f"Expected {expected} but got {first_unique}"

# Test 2: Multiple characters, all unique
s = 'abcd'
first_unique = Solution().firstUniqChar(s)
expected = 0
assert first_unique == expected, f"Expected {expected} but got {first_unique}"

# Test 3: Multiple characters, no unique
s = 'aabbccdd'
first_unique = Solution().firstUniqChar(s)
expected = -1
assert first_unique == expected, f"Expected {expected} but got {first_unique}"

# Test 4: Multiple characters with unique
s = 'aabccd'
first_unique = Solution().firstUniqChar(s)
expected = 2
assert first_unique == expected, f"Expected {expected} but got {first_unique}"