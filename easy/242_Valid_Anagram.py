from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)


"""
Explanation:

Return True if the frequency of all characters in input string "s" are the same as input string "t". Else, return False.

Notes:

Time complexity: O(s + t), where s and t are the lengths of the 2 input strings.

Space complexity: O(1), as we store at most 26 letters in each counter.
"""

# Test 1: Both strings single character, not valid
s = 'a'
t = 'b'
is_anagram = Solution().isAnagram(s, t)
expected = False
assert is_anagram == expected, f"Expected {expected} but got {is_anagram}"

# Test 2: Both strings single character, valid
s = 'a'
t = 'a'
is_anagram = Solution().isAnagram(s, t)
expected = True
assert is_anagram == expected, f"Expected {expected} but got {is_anagram}"

# Test 3: Both strings same length, valid
s = 'abab'
t = 'baba'
is_anagram = Solution().isAnagram(s, t)
expected = True
assert is_anagram == expected, f"Expected {expected} but got {is_anagram}"

# Test 4: Both strings same length, not valid
s = 'abac'
t = 'acca'
is_anagram = Solution().isAnagram(s, t)
expected = False
assert is_anagram == expected, f"Expected {expected} but got {is_anagram}"

# Test 5: Different length strings, not valid
s = 'abcd'
t = 'ab'
is_anagram = Solution().isAnagram(s, t)
expected = False
assert is_anagram == expected, f"Expected {expected} but got {is_anagram}"
