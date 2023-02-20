class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        dp = [[False] * (len(s2) + 1) for _ in range(len(s1) + 1)]
        dp[-1][-1] = True

        for i in reversed(range(len(s1) + 1)):
            for j in reversed(range(len(s2) + 1)):
                if i < len(s1) and s1[i] == s3[i + j] and dp[i + 1][j]:
                    dp[i][j] = True
                if j < len(s2) and s2[j] == s3[i + j] and dp[i][j + 1]:
                    dp[i][j] = True

        return dp[0][0]


"""
Explanation:

Check if the length of s1 and s2 add up to the length of s3, if not, then s3 can't be formed by interleaving s1 and s2. Initialize a 2D array dp with False values of size (len(s1)+1) x (len(s2)+1). dp[i][j] indicates whether s3[0:i+j] can be formed by interleaving the first i characters of s1 and the first j characters of s2. Set the value of dp[-1][-1] to True, because an empty string can be formed by interleaving two empty strings. Then iterate over the 2D array dp in reverse order. For each i and j, check whether the next character in s3 can be formed by interleaving the current character in s1 with the subsequence of s3 that can be formed by the current subsequence of s2, or by interleaving the current character in s2 with the subsequence of s3 that can be formed by the current subsequence of s1. If either of these two conditions is met, set the value of dp[i][j] to True. Finally, return dp[0][0], which indicates whether the entire s3 can be formed by interleaving s1 and s2.

Notes:

Time complexity: O(len(s1) * len(s2)), since we need to iterate through a 2D array of size len(s1) * len(s2).

Space complexity: O(len(s1) * len(s2)), since we need to create a 2D array of size len(s1) * len(s2) to store intermediate results.
"""

# Test 1: s1 and s2 empty, s3 empty
s1 = ''
s2 = ''
s3 = ''
is_interleave = Solution().isInterleave(s1, s2, s3)
expected = True
assert is_interleave == expected, f"Expected {expected} but got {is_interleave}"

# Test 2: s1 and s2 empty, s3 not empty
s1 = ''
s2 = ''
s3 = 'abc'
is_interleave = Solution().isInterleave(s1, s2, s3)
expected = False
assert is_interleave == expected, f"Expected {expected} but got {is_interleave}"

# Test 3: s1 and s2 not empty, s3 empty
s1 = 'abc'
s2 = 'abc'
s3 = ''
is_interleave = Solution().isInterleave(s1, s2, s3)
expected = False
assert is_interleave == expected, f"Expected {expected} but got {is_interleave}"

# Test 4: s1 empty, s2 equals s3
s1 = ''
s2 = 'abc'
s3 = 'abc'
is_interleave = Solution().isInterleave(s1, s2, s3)
expected = True
assert is_interleave == expected, f"Expected {expected} but got {is_interleave}"

# Test 5: s2 empty, s1 equals s3
s1 = 'abc'
s2 = ''
s3 = 'abc'
is_interleave = Solution().isInterleave(s1, s2, s3)
expected = True
assert is_interleave == expected, f"Expected {expected} but got {is_interleave}"

# Test 6: s1 and s2 not empty, valid interleave
s1 = 'abc'
s2 = 'abc'
s3 = 'ababcc'
is_interleave = Solution().isInterleave(s1, s2, s3)
expected = True
assert is_interleave == expected, f"Expected {expected} but got {is_interleave}"

# Test 7: s1 and s2 not empty, not valid interleave
s1 = 'abc'
s2 = 'abc'
s3 = 'abcdef'
is_interleave = Solution().isInterleave(s1, s2, s3)
expected = False
assert is_interleave == expected, f"Expected {expected} but got {is_interleave}"

# Test 8: All same string
s1 = 'abc'
s2 = 'abc'
s3 = 'abcabc'
is_interleave = Solution().isInterleave(s1, s2, s3)
expected = True
assert is_interleave == expected, f"Expected {expected} but got {is_interleave}"

# Test 9: All different strings
s1 = 'abc'
s2 = 'def'
s3 = 'ghijkl'
is_interleave = Solution().isInterleave(s1, s2, s3)
expected = False
assert is_interleave == expected, f"Expected {expected} but got {is_interleave}"
