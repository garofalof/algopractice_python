class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m + 1):
            dp[i][0] = i

        for j in range(n + 1):
            dp[0][j] = j

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])

        return dp[m][n]

"""
Explanation:

We create a 2D matrix `dp` of size `(m+1) x (n+1)`, where `m` and `n` are the lengths of `word1` and `word2`, respectively. Each cell `dp[i][j]` represents the minimum number of operations required to transform the first `i` characters of `word1` into the first `j` characters of `word2`.

We start by initializing the base cases: `dp[i][0] = i` represents the number of operations required to transform the first `i` characters of `word1` into an empty string, and `dp[0][j] = j` represents the number of operations required to transform an empty string into the first `j` characters of `word2`. Next, we iterate through the remaining cells of the matrix. For each cell `dp[i][j]`, if the characters at positions `i-1` and `j-1` in `word1` and `word2` are equal, we assign `dp[i][j]` the value from the diagonal cell `dp[i-1][j-1]` since no operation is needed. Otherwise, we assign `dp[i][j]` the minimum value from the adjacent cells (`dp[i-1][j]`, `dp[i][j-1]`, `dp[i-1][j-1]`) plus one to account for the cost of the operation.

Finally, we return `dp[m][n]`, which represents the minimum number of operations required to transform `word1` into `word2`.

Notes:

Time complexity: O(m*n), where m and n are the lengths of `word1` and `word2`, respectively

Space complexity: O(m*n), as we create a 2D matrix of size `(m+1) x (n+1)` to store the intermediate results
"""

# Test Case 1: Word1 and Word2 are empty strings
word1 = ""
word2 = ""
result = Solution().minDistance(word1, word2)
expected = 0
assert result == expected, f"Expected {expected} but got {result}"

# Test Case 2: Word1 and Word2 are equal
word1 = "abc"
word2 = "abc"
result = Solution().minDistance(word1, word2)
expected = 0
assert result == expected, f"Expected {expected} but got {result}"

# Test Case 3: Word1 and Word2 have different lengths
word1 = "horse"
word2 = "ros"
result = Solution().minDistance(word1, word2)
expected = 3
assert result == expected, f"Expected {expected} but got {result}"

# Test Case 4: Word1 and Word2 have no common characters
word1 = "abcd"
word2 = "efgh"
result = Solution().minDistance(word1, word2)
expected = 4
assert result == expected, f"Expected {expected} but got {result}"

# Test Case 5: Word1 and Word2 have some common characters
word1 = "intention"
word2 = "execution"
result = Solution().minDistance(word1, word2)
expected = 5
assert result == expected, f"Expected {expected} but got {result}"

# Test Case 6: Word1 is an empty string
word1 = ""
word2 = "algorithm"
result = Solution().minDistance(word1, word2)
expected = len(word2)
assert result == expected, f"Expected {expected} but got {result}"

# Test Case 7: Word2 is an empty string
word1 = "programming"
word2 = ""
result = Solution().minDistance(word1, word2)
expected = len(word1)
assert result == expected, f"Expected {expected} but got {result}"
