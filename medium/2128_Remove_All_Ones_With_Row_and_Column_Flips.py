from typing import List


class Solution:
    def removeOnes(self, grid: List[List[int]]) -> bool:
        rows, cols = len(grid), len(grid[0])

        for r in range(1, rows):
            for c in range(cols):
                curr = grid[r][c]
                first_row_start = grid[0][0]
                curr_row_start = grid[r][0]
                curr_col_start = grid[0][c]

                if curr_row_start == first_row_start:
                    if curr != curr_col_start:
                        return False
                else:
                    if curr != 1 - curr_col_start:
                        return False

        return True


"""
Explanation:

Initialize the number of rows and cols. For each element in the grid starting from the second row: Compare the start value of the current row with the start value of the first row. If they are equal, compare the current value with the value in the first row in the same column. If they are not equal, return False. If the start values are not equal, compare the current value with 1 minus the value in the first row in the same column. If they are not equal, return False. After iterating through all elements in the grid, return True.

Notes:

Time complexity: O(m * n)

Space complexity: O(1)
"""

# Test 1: Single element
grid = [[1]]
can_remove = Solution().removeOnes(grid)
expected = True
assert can_remove == expected, f"Expected {expected} but got {can_remove}"

# Test 2: Multiple rows, same element
grid = [[1, 1], [1, 1]]
can_remove = Solution().removeOnes(grid)
expected = True
assert can_remove == expected, f"Expected {expected} but got {can_remove}"

# Test 3: Same row start, different column start
grid = [[1, 0, 1], [1, 1, 1]]
can_remove = Solution().removeOnes(grid)
expected = False
assert can_remove == expected, f"Expected {expected} but got {can_remove}"

# Test 4: Same row start, same column start
grid = [[0, 1, 1], [0, 1, 1]]
can_remove = Solution().removeOnes(grid)
expected = True
assert can_remove == expected, f"Expected {expected} but got {can_remove}"

# Test 5: Different row start, different column start
grid = [[0, 1], [1, 0]]
can_remove = Solution().removeOnes(grid)
expected = True
assert can_remove == expected, f"Expected {expected} but got {can_remove}"

# Test 6: Different row start, same column start
grid = [[0, 1], [1, 1]]
can_remove = Solution().removeOnes(grid)
expected = False
assert can_remove == expected, f"Expected {expected} but got {can_remove}"
