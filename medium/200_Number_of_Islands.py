from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            if r < 0 or c < 0 or r == rows or c == cols or grid[r][c] == "0":
                return

            grid[r][c] = "0"
            dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                dfs(nr, nc)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    dfs(r, c)
                    count += 1

        return count

"""
Explanation:

Initialize island count to 0 and set variables `rows` and `cols` to number of rows and columns in grid. For each node in grid: if island is encountered, increase island count by 1 and perform dfs to mark island nodes as visited. Once done traversing grid, return final island count.

Notes:

Time complexity: O(rows * columns), as we traverse each node in the grid at most once

Space complexity: O(rows * columns), as we create a call stack that can go as deep as the number of cells in the grid in the worst case
"""

# Test Case 1: Single island
grid = [
    ["1", "1", "1"],
    ["1", "1", "1"],
    ["1", "1", "1"]
]
result = Solution().numIslands(grid)
expected = 1
assert result == expected, f"Expected {expected} but got {result}"

# Test Case 2: Multiple islands disconnected
grid = [
    ["1", "0", "1"],
    ["0", "1", "0"],
    ["1", "0", "1"]
]
result = Solution().numIslands(grid)
expected = 5
assert result == expected, f"Expected {expected} but got {result}"

# Test Case 3: No islands
grid = [
    ["0", "0", "0"],
    ["0", "0", "0"],
    ["0", "0", "0"]
]
result = Solution().numIslands(grid)
expected = 0
assert result == expected, f"Expected {expected} but got {result}"

# Test Case 4: Multiple islands, some connected
grid = [
    ["1", "0", "1"],
    ["1", "1", "0"],
    ["1", "0", "1"]
]
result = Solution().numIslands(grid)
expected = 3
assert result == expected, f"Expected {expected} but got {result}"

# Test Case 5: Single island, single node
grid = [["1"]]
result = Solution().numIslands(grid)
expected = 1
assert result == expected, f"Expected {expected} but got {result}"