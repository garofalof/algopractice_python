from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        def countNeighbors(r, c, dirs):
            count = 0

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc

                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] in (1, 3):
                    count += 1

            return count

        dirs = [(dr, dc) for dr in (-1, 0, 1) for dc in (-1, 0, 1)]
        dirs.remove((0, 0))

        rows = len(board)
        cols = len(board[0])

        for r in range(rows):
            for c in range(cols):
                count = countNeighbors(r, c, dirs)

                if board[r][c] == 1 and count in (2, 3):
                    board[r][c] = 3
                elif board[r][c] == 0 and count == 3:
                    board[r][c] = 2

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 1:
                    board[r][c] = 0
                elif board[r][c] in (2, 3):
                    board[r][c] = 1


"""
Explanation:

Create a list of all possible directions to check for neighbors (excluding the cell itself) and then iterate over this list for each cell. For each neighbor, check if it's within the bounds of the board and if it's alive (1) or was alive (3) in the previous state of the board, and increment the neighbor count accordingly.

After counting the neighbors for each cell, update the board according to the rules of the game. If a live cell has 2 or 3 live neighbors, it remains alive, otherwise it dies. If a dead cell has exactly 3 live neighbors, it becomes alive. To avoid modifying the current state of the board while counting neighbors, use a separate encoding where a cell that was alive in the previous state is represented by 3 and a cell that was dead is represented by 2.

Finally, iterate over the board and replace all cells that are 1 or 3 with 1 (live), and all other cells with 0 (dead).

Notes:

Time Complexity: O(m * n), where m and n are the dimensions of the board
Space Complexity: O(1)
"""

# Test 1: Live cell with < 2 live neighbors
board = [[1]]
expected = [[0]]
Solution().gameOfLife(board)
assert board == expected, f"Expected {expected} but got {board}"

# Test 2: Dead cell with < 2 live neighbors
board = [[0]]
expected = [[0]]
Solution().gameOfLife(board)
assert board == expected, f"Expected {expected} but got {board}"

# Test 3: Live cell w/ 2 live neighbors
board = [[1, 0], [1, 1]]
expected = [[1, 1], [1, 1]]
Solution().gameOfLife(board)
assert board == expected, f"Expected {expected} but got {board}"

# Test 4: Live cell w/ 3 live neighbors
board = [[1, 1], [1, 1]]
expected = [[1, 1], [1, 1]]
Solution().gameOfLife(board)
assert board == expected, f"Expected {expected} but got {board}"

# Test 5: Live cell w/ > 3 live neighbors
board = [[1, 1, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0]]
expected = [[1, 1, 0, 0], [1, 0, 0, 0], [0, 0, 0, 0]]
Solution().gameOfLife(board)
assert board == expected, f"Expected {expected} but got {board}"

# Test 5: Dead cell w/ 3 live neighbors
board = [[0, 1], [1, 1]]
expected = [[1, 1], [1, 1]]
Solution().gameOfLife(board)
assert board == expected, f"Expected {expected} but got {board}"
