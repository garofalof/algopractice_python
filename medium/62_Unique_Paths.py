class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] * n

        for r in reversed(range(m - 1)):
            for c in reversed(range(n - 1)):
                dp[c] += dp[c + 1]

        return dp[0]


"""
Explanation:

The dp list is initialized with 1 for each column, representing the number of unique paths from the start to each point along the bottom row.

Starting from the second-to-last row and second-to-last column, iteratively update the dp list by summing the number of unique paths from the point directly below and the point directly to the right.

After iterating through all the rows and columns, the value in the first column of the dp list represents the number of unique paths from the start to the end of the grid. Return this value.

Notes:

Time complexity: O(m * n), where m and n represent the number of rows and columns in the grid.

Space complexity: O(n), where n is the number of columns in the grid used to hold the dp array.
"""

# Test 1: Min values
m = 1
n = 1
unique_paths = Solution().uniquePaths(m, n)
expected = 1
assert unique_paths == expected, f"Expected {expected} but got {unique_paths}"

# Test 2: Max values
m = 100
n = 100
unique_paths = Solution().uniquePaths(m, n)
expected = 22750883079422934966181954039568885395604168260154104734000
assert unique_paths == expected, f"Expected {expected} but got {unique_paths}"

# Test 3: Square matrix
m = 4
n = 4
unique_paths = Solution().uniquePaths(m, n)
expected = 20
assert unique_paths == expected, f"Expected {expected} but got {unique_paths}"

# Test 4: Rectangular matrix
m = 3
n = 7
unique_paths = Solution().uniquePaths(m, n)
expected = 28
assert unique_paths == expected, f"Expected {expected} but got {unique_paths}"
