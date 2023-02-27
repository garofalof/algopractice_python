from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        max_area = 0

        def dfs(r, c):
            if r < 0 or r == rows or c < 0 or c == cols or not grid[r][c]:
                return 0

            grid[r][c] = 0

            return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]:
                    max_area = max(max_area, dfs(r, c))

        return max_area


"""
Explanation:

Use a dfs algorithm to traverse through the grid and find the area of the largest island. For each island node in the grid, the helper dfs function is called recursively to check the neighboring cells of the current cell and mark them as visited by setting their value to 0. The function returns the size of the island, which is then compared to the current maximum area to find the largest island in the grid.

Notes:

Time complexity: O(rows * cols), as each cell is visited at most once.

Space complexity: O(rows * cols), as the recursive calls to dfs can potentially fill up the call stack with O(rows * cols) function calls.
"""

# Test 1: 1 x 1, island
grid = [[1]]
max_area = Solution().maxAreaOfIsland(grid)
expected = 1
assert max_area == expected, f"Expected {expected} but got {max_area}"

# Test 2: 1 x 1, no island
grid = [[0]]
max_area = Solution().maxAreaOfIsland(grid)
expected = 0
assert max_area == expected, f"Expected {expected} but got {max_area}"

# Test 3: No island
grid = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
max_area = Solution().maxAreaOfIsland(grid)
expected = 0
assert max_area == expected, f"Expected {expected} but got {max_area}"

# Test 4: All island
grid = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]
max_area = Solution().maxAreaOfIsland(grid)
expected = 16
assert max_area == expected, f"Expected {expected} but got {max_area}"

# Test 5: Island zig zag
grid = [[1, 0, 0, 1], [0, 0, 0, 1], [0, 0, 1, 1], [1, 1, 1, 0]]
max_area = Solution().maxAreaOfIsland(grid)
expected = 7
assert max_area == expected, f"Expected {expected} but got {max_area}"

# Test 6: Island middle
grid = [[1, 0, 0, 0], [0, 1, 1, 0], [0, 1, 1, 0], [1, 0, 0, 1]]
max_area = Solution().maxAreaOfIsland(grid)
expected = 4
assert max_area == expected, f"Expected {expected} but got {max_area}"

# Test 7: Island mixed
grid = [[1, 1, 0, 0, 0], [1, 0, 1, 1, 1], [0, 1, 1, 0, 0], [0, 1, 0, 0, 1]]
max_area = Solution().maxAreaOfIsland(grid)
expected = 6
assert max_area == expected, f"Expected {expected} but got {max_area}"
