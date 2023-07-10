import heapq
from typing import List


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = set()
        heap = []
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        result = 0

        visited.add((0, 0))
        heapq.heappush(heap, (grid[0][0], 0, 0))

        while heap:
            depth, row, col = heapq.heappop(heap)
            result = max(result, depth)

            if row == n - 1 and col == n - 1:
                return result

            for dr, dc in directions:
                newR = row + dr
                newC = col + dc
                key = (newR, newC)

                if 0 <= newR < n and 0 <= newC < n and key not in visited:
                    heapq.heappush(heap, (grid[newR][newC], newR, newC))
                    visited.add(key)

        return result


"""
Explanation:

Initialize a heap to store cells along w/ their respective depths. The cells with lower depths are given higher priority in the heap. Initialize a `visited` set to keep track of visited cells. Initialize a `directions` list to define the possible movement directions: right, down, left, and up. Initialize a `result` variable to store the max depth encountered during the traversal, which represents the max time needed to reach the current cell. Start by adding the top-left cell (0, 0) to the heap with its corresponding depth from the grid[0][0].

While the heap is not empty, pop the cell with the minimum depth from the heap. If the popped cell is the bottom-right cell (n-1, n-1), the max depth encountered so far is returned as the minimum time to swim. Else, explore the adjacent cells. If an adjacent cell is within the grid bounds and has not been visited, it is added to the heap with its corresponding and marked as visited. The process continues until the bottom-right cell is reached or until all cells have been explored.

Finally, the max depth encountered during the traversal is returned as the minimum time required to swim from the top-left to the bottom-right cell.

Notes:

Time complexity: O(n ^ 2 * log n), as we visit each cell in the grid at most once and do max one log n insertion at each ndoe

Space complexity: O(n ^ 2) for both the heap and visited set
"""

# Test Case 1: Minimum grid size
grid = [[0]]
result = Solution().swimInWater(grid)
expected = 0
assert result == expected, f"Expected {expected} but got {result}"

# Test Case 2: Grid size 2x2
grid = [[0, 1], [3, 2]]
result = Solution().swimInWater(grid)
expected = 2
assert result == expected, f"Expected {expected} but got {result}"

# Test Case 3: Grid size 3x3, increasing values
grid = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
result = Solution().swimInWater(grid)
expected = 8
assert result == expected, f"Expected {expected} but got {result}"

# Test Case 4: Grid size 3x3, random values
grid = [[1, 2, 3], [8, 9, 4], [7, 6, 5]]
result = Solution().swimInWater(grid)
expected = 5
assert result == expected, f"Expected {expected} but got {result}"

# Test Case 5: Grid size 4x4, increasing values
grid = [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]]
result = Solution().swimInWater(grid)
expected = 15
assert result == expected, f"Expected {expected} but got {result}"

# Test Case 6: Grid size 4x4, random values
grid = [[4, 2, 1, 0], [5, 6, 8, 7], [10, 11, 9, 12], [13, 15, 14, 3]]
result = Solution().swimInWater(grid)
expected = 12
assert result == expected, f"Expected {expected} but got {result}"
