from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pacific, atlantic = set(), set()

        def dfs(r, c, memo):
            memo.add((r, c))
            dirs = [(r + 1, c), (r, c + 1), (r - 1, c), (r, c - 1)]

            for nr, nc in dirs:
                if 0 <= nr < rows and 0 <= nc < cols and heights[nr][nc] >= heights[r][c] and (nr, nc) not in memo:
                    dfs(nr, nc, memo)

        for row in range(rows):
            dfs(row, 0, pacific)
            dfs(row, cols - 1, atlantic)

        for col in range(cols):
            dfs(0, col, pacific)
            dfs(rows - 1, col, atlantic)

        return list(pacific & atlantic)


"""
Explanation:

Initialize two sets to keep track of the cells that can be reached by the Pacific and Atlantic oceans, respectively. Then, perform DFS starting from each cell in the first and last columns, marking all the cells that can be reached by the Pacific and Atlantic oceans, respectively. Then, do the same starting from each cell in the first and last rows. Finally, return a list of the cells that are present in both sets, meaning that rain water can flow from those cells to both oceans.

Notes:

Time complexity: O(m x n), where m is the number of rows and n is the number of columns, as the DFS function runs exactly once for each cell accessible from the ocean.

Space complexity: O(m x n), as we use m x n space on the recursion stack, as well as the sets used to keep track of the cells that can be reached by the oceans.
"""

# Test 1: Simple square grid
heights = [[1, 2, 3],
           [2, 3, 1],
           [3, 1, 2]]
rain_flow = Solution().pacificAtlantic(heights)
expected = [(1, 1), (2, 0), (0, 2)]
assert rain_flow == expected, f"Expected {expected} but got {rain_flow}"

# Test 2: All cells same height
heights = [[5, 5],
           [5, 5]]
rain_flow = Solution().pacificAtlantic(heights)
expected = [(0, 1), (1, 0), (1, 1), (0, 0)]
assert rain_flow == expected, f"Expected {expected} but got {rain_flow}"

# Test 3: Single row
heights = [[1, 2, 3, 4, 5]]
rain_flow = Solution().pacificAtlantic(heights)
expected = [(0, 1), (0, 4), (0, 0), (0, 3), (0, 2)]
assert rain_flow == expected, f"Expected {expected} but got {rain_flow}"

# Test 4: Single column
heights = [[5],
           [4],
           [3],
           [2],
           [1]]
rain_flow = Solution().pacificAtlantic(heights)
expected = [(4, 0), (0, 0), (2, 0), (3, 0), (1, 0)]
assert rain_flow == expected, f"Expected {expected} but got {rain_flow}"

# Test 5: Random grid
heights = [[1, 2, 2, 3, 5],
           [3, 2, 3, 4, 4],
           [2, 4, 5, 3, 1],
           [6, 7, 1, 4, 5],
           [5, 1, 1, 2, 4]]
rain_flow = Solution().pacificAtlantic(heights)
expected = [(4, 0), (0, 4), (3, 1), (1, 4), (3, 0), (2, 2), (1, 3)]
assert rain_flow == expected, f"Expected {expected} but got {rain_flow}"
