import collections
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = collections.deque()
        rows, cols = len(grid), len(grid[0])
        fresh_count = 0
        max_time = 0

        for r in range(rows):
            for c in range(cols):
                node = grid[r][c]
                fresh_count += node == 1

                if node == 2:
                    q.append((r, c, 0))

        while q:
            r, c, elapsed = q.popleft()
            max_time = max(max_time, elapsed)
            dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc

                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    fresh_count -= 1
                    q.append((nr, nc, elapsed + 1))

        return max_time if not fresh_count else -1

"""
Explanation:

Initialize a queue, get number of rows and columns, and set count of fresh oranges and max time elapsed to 0. Iterate over grid to add rotten oranges to queue and count the number of fresh oranges. While queue has work, pop the current node from the front and update max time elapsed to the greater of current node's elapsed time or max time elapsed. For each direction up, down, left, and right, check if fresh neighbor exists and, if so, mark rotten, decrease fresh count, and add coordinates w/ increased time to queue. Once done, return the max elapsed time if all oranges rotten, else return -1.

Notes:

Time complexity: O(rows * cols)

Space complexity: O(rows * cols)
"""

# Test Case 1: 1 x 1 grid, no rotten
grid = [[1]]
result = Solution().orangesRotting(grid)
expected = -1
assert result == expected, f"Expected {expected} but got {result}"

# Test Case 2: 1 x 1 grid, rotten
grid = [[2]]
result = Solution().orangesRotting(grid)
expected = 0
assert result == expected, f"Expected {expected} but got {result}"

# Test Case 3: All rotten
grid = [[2, 2, 2], [2, 2, 2], [2, 2, 2]]
result = Solution().orangesRotting(grid)
expected = 0
assert result == expected, f"Expected {expected} but got {result}"

# Test Case 4: All fresh
grid = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
result = Solution().orangesRotting(grid)
expected = -1
assert result == expected, f"Expected {expected} but got {result}"

# Test Case 5: Some rotten and some fresh
grid = [[1, 2, 2], [1, 1, 2], [2, 1, 1]]
result = Solution().orangesRotting(grid)
expected = 1
assert result == expected, f"Expected {expected} but got {result}"

# Test Case 6: Some rotten, some fresh, and some empty
grid = [[0, 2, 2], [0, 1, 2], [2, 1, 0]]
result = Solution().orangesRotting(grid)
expected = 1
assert result == expected, f"Expected {expected} but got {result}"

# Test Case 7: Failure case
grid = [[0, 1, 0], [2, 0, 1], [2, 0, 1]]
result = Solution().orangesRotting(grid)
expected = -1
assert result == expected, f"Expected {expected} but got {result}"