class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = {}

        def dfs(i: int, j: int) -> int:
            if (i, j) in dp:
                return dp[(i, j)]
            if j == len(t):
                return 1

            if i == len(s):
                return 0

            count = 0

            if s[i] == t[j]:
                count = dfs(i + 1, j + 1) + dfs(i + 1, j)
            else:
                count = dfs(i + 1, j)

            dp[(i, j)] = count

            return count

        return dfs(0, 0)

"""
Explanation:

Keep track of the computed results using a dictionary dp to avoid redundant computations. Perform dfs on starting indices of both strings. If index pair has been visited, return count at index. If we've reached end of string t, subsequence has been found so return 1. If we've reached end of s without reaching end of t, return 0 as no subsequence found. If characters at current index pair are same, set count to result of performing dfs by increasing both indices by 1, as well as just increasing s by 1. Else set count to dfs to result of increasing index in string s by 1. Once done, set count in dictionary for pair and return count to function call.

Notes:

Time complexity: O(len(s) * len(t))
Space complexity: O(len(s) * len(t))
"""

# Test Case 1: Same strings
s = 'rabbit'
t = 'rabbit'
result = Solution().numDistinct(s, t)
expected = 1
assert result == expected, f'Expected {expected} but got {result}'

# Test Case 2: No distinct subsequences
s = 'abc'
t = 'def'
result = Solution().numDistinct(s, t)
expected = 0
assert result == expected, f'Expected {expected} but got {result}'

# Test Case 3: Multiple distinct subsequences
s = 'bagagabag'
t = 'bag'
result = Solution().numDistinct(s, t)
expected = 8
assert result == expected, f'Expected {expected} but got {result}'

# Test Case 4: Repeated characters
s = 'aaaaaa'
t = 'aaa'
result = Solution().numDistinct(s, t)
expected = 20
assert result == expected, f'Expected {expected} but got {result}'