from typing import Counter, List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_count, s_count = Counter(p), Counter(s[:len(p)])
        result = [0] if p_count == s_count else []

        for i, char in enumerate(s[len(p):]):
            s_char = s[i]
            s_count[char] += 1
            s_count[s_char] -= 1

            if not s_count[s_char]:
                del s_count[s_char]

            if p_count == s_count:
                result.append(i + 1)

        return result


"""
Explanation:

Create two Counter objects, one for p and one for a substring of s of the same length as p. Then compare these two Counters to see if they are equal. If they are, the starting index of the substring is appended to the output list.

Now iterate over the rest of s using a sliding window of length len(p) onwards. For each iteration, add the new character to the s_count Counter, and removes the first character in the window from the Counter. Then check if the count of that removed character is 0, and if it is, delete that key-value pair from the Counter. If the two Counters are now equal, append the starting index of the current window to the output list.

Finally, return the output list containing the starting indices of all anagrams of p in s.

Notes:

Time complexity: O(n), where n is the length of input string s.

Space complexity: O(1), as the counters are constrained to 26 characters.
"""

# Test 1: Both strings single character, no anagrams
s = 'a'
p = 'b'
anagram_indices = Solution().findAnagrams(s, p)
expected = []
assert anagram_indices == expected, f"Expected {expected} but got {anagram_indices}"

# Test 2: Both strings single character, anagram
s = 'a'
p = 'a'
anagram_indices = Solution().findAnagrams(s, p)
expected = [0]
assert anagram_indices == expected, f"Expected {expected} but got {anagram_indices}"

# Test 3: s shorter than p
s = 'abc'
p = 'abcd'
anagram_indices = Solution().findAnagrams(s, p)
expected = []
assert anagram_indices == expected, f"Expected {expected} but got {anagram_indices}"

# Test 4: s == p
s = 'abc'
p = 'abc'
anagram_indices = Solution().findAnagrams(s, p)
expected = [0]
assert anagram_indices == expected, f"Expected {expected} but got {anagram_indices}"

# Test 5: No valid anagrams
s = 'abcdef'
p = 'xyz'
anagram_indices = Solution().findAnagrams(s, p)
expected = []
assert anagram_indices == expected, f"Expected {expected} but got {anagram_indices}"

# Test 6: Multiple valid anagrams
s = 'cbadefgabc'
p = 'abc'
anagram_indices = Solution().findAnagrams(s, p)
expected = [0, 7]
assert anagram_indices == expected, f"Expected {expected} but got {anagram_indices}"
