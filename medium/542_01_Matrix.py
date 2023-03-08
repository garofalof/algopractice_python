import collections
from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        q = collections.deque()
        rows, cols = len(mat), len(mat[0])

        for r in range(rows):
            for c in range(cols):
                node = mat[r][c]

                if node == 0:
                    q.append((r, c))
                else:
                    mat[r][c] = -1
        while q:
            r, c = q.popleft()

            for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                if 0 <= nr < rows and 0 <= nc < cols and mat[nr][nc] == -1:
                    mat[nr][nc] = mat[r][c] + 1
                    q.append((nr, nc))

        return mat


"""
Explanation:

Initialize a queue and set the number of rows and columns in the matrix.

Then iterate over every cell in the matrix and check if the cell value is zero. If the cell value is zero, add the cell coordinates to the queue. If the cell value is not zero, set the cell value to -1, indicating that the cell has not yet been visited.

Next, deque a cell from the queue and checks its neighboring cells to see if they have not been visited before. If a neighboring cell has not been visited before, set its value to the distance of the dequed cell plus one, and then add the neighboring cell to the queue.  Repeat this process until the queue is empty.

Finally, return the updated matrix with the minimum distances to the nearest zero for each cell.

Notes:

Time complexity: O(rows * cols), where rows and cols are the number of rows and columns in the matrix, respectively.

Space complexity: O(rows * cols), where rows and cols are the number of rows and columns in the matrix, respectively.
"""

# Test 1: 1 x 1, node is 0
matrix = [[0]]
updated_matrix = Solution().updateMatrix(matrix)
expected = [[0]]
assert updated_matrix == expected, f"Expected {expected} but got {updated_matrix}"

# Test 2: 2 x 2, input same as output
matrix = [[0, 1], [1, 0]]
updated_matrix = Solution().updateMatrix(matrix)
expected = [[0, 1], [1, 0]]
assert updated_matrix == expected, f"Expected {expected} but got {updated_matrix}"

# Test 3: 3 x 3, input same as output
matrix = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
updated_matrix = Solution().updateMatrix(matrix)
expected = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
assert updated_matrix == expected, f"Expected {expected} but got {updated_matrix}"

# Test 4: 3 x 3, test distance > 1
matrix = [[0, 0, 0], [0, 1, 0], [1, 1, 1]]
updated_matrix = Solution().updateMatrix(matrix)
expected = [[0, 0, 0], [0, 1, 0], [1, 2, 1]]
assert updated_matrix == expected, f"Expected {expected} but got {updated_matrix}"

# Test 5: 4 x 4, test distance > 1
matrix = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 0, 1], [1, 1, 1, 1]]
updated_matrix = Solution().updateMatrix(matrix)
expected = [[4, 3, 2, 3], [3, 2, 1, 2], [2, 1, 0, 1], [3, 2, 1, 2]]
assert updated_matrix == expected, f"Expected {expected} but got {updated_matrix}"
