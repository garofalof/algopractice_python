from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        self.dp = {}
        longest = 0

        def dfs(r, c, prev):
            key = (r, c)
            result = 1

            if r < 0 or c < 0 or r == rows or c == cols or matrix[r][c] <= prev:
                return 0
            if key in self.dp:
                return self.dp.get(key)

            dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc

                result = max(result, 1 + dfs(nr, nc, matrix[r][c]))

            self.dp[key] = result

            return result

        for r in range(rows):
            for c in range(cols):
                longest = max(longest, dfs(r, c, -1))

        return longest

"""
Explanation:

Initialize rows and cols to keep count of the number of rows and columns in the matrix, respectively. The dp dictionary is used to store the memoization of previously calculated results. It maps a position (r, c) to the length of the longest increasing path starting from that position. The longest variable is initialized to 0 and will be used to keep track of the max length found so far.

The dfs function is defined to perform depth-first search and calculate the length of the increasing path from a given position (r, c) with a previous value prev. Inside the function, a key is created from the current position (r, c) and checked in the dp dictionary. If the result for that position is already memoized, it is returned. The result variable is initialized to 1, as the current position is considered part of the increasing path. The dirs variable holds the four possible directions (right, down, left, up) in which to explore the neighbors of the current position. The function then iterates over each direction and calculates the new neighbor position (nr, nc). If the neighbor position is valid (within the matrix boundaries) and the value at the neighbor position < the previous value, the result is updated by adding 1 to the result of the recursive call to dfs on the neighbor position. After exploring all valid neighbors, the result is stored in the dp dictionary for the current position and returned as the result.

The main loop iterates over each position in the matrix using nested for loops and calls the dfs function to calculate the longest increasing path starting from that position.
The longest variable is updated with the max length found so far.

Finally, the longest value is returned as the result.

Notes:

Time complexity: O(rows * cols), as we visit each cell in the matrix at most once

Space complexity: O(rows * cols) for both dp dictionary and recursion stack
"""

# Test Case 1: 1 x 1 grid, single element
grid = [[5]]
result = Solution().longestIncreasingPath(grid)
expected = 1
assert result == expected, f"Expected {expected} but got {result}"

# Test Case 2: 2 x 2 grid, all elements are the same
grid = [
    [3, 3],
    [3, 3]
]
result = Solution().longestIncreasingPath(grid)
expected = 1
assert result == expected, f"Expected {expected} but got {result}"

# Test Case 3: 3 x 3 grid, no increasing path
grid = [
    [2, 2, 2],
    [2, 2, 2],
    [2, 2, 2]
]
result = Solution().longestIncreasingPath(grid)
expected = 1
assert result == expected, f"Expected {expected} but got {result}"

# Test Case 4: 3 x 3 grid, increasing path covers entire grid
grid = [
    [1, 2, 3],
    [6, 5, 4],
    [7, 8, 9]
]
result = Solution().longestIncreasingPath(grid)
expected = 9
assert result == expected, f"Expected {expected} but got {result}"

# Test Case 5: 4 x 4 grid, complex increasing path
grid = [
    [9, 9, 4, 3],
    [6, 6, 8, 1],
    [2, 1, 1, 7],
    [5, 3, 6, 2]
]
result = Solution().longestIncreasingPath(grid)
expected = 4
assert result == expected, f"Expected {expected} but got {result}"
