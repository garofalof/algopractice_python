from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])

        def dfs(r, c):
            board[r][c] = '*'

            for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == 'O':
                    dfs(nr, nc)

        for r in range(rows):
            for c in range(cols):
                if (r in (0, rows - 1) or c in (0, cols - 1)) and board[r][c] == 'O':
                    dfs(r, c)
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == '*':
                    board[r][c] = 'O'
                else:
                    board[r][c] = 'X'


"""
Explanation:

The algorithm performs a depth-first search starting from all boundary points with 'O' values. These boundary points are identified by checking the first and last row and column of the board.

During the DFS, all visited 'O' points are replaced with '*' to mark them as visited. Once all 'O' points reachable from a boundary point have been marked with '*', we then iterate through the entire board again and replace all remaining 'O' points with 'X' since these points are not connected to any boundary 'O' points and hence are surrounded by 'X'. We also replace all '*' with 'O' since these were initially 'O' points that are not surrounded by 'X'.

Notes:

Time complexity: O(m * n), where m and n represent the number of rows and columns in the board.

Space complexity: O(m * n) in the worst case if all points are initially 'O' and hence are visited during the DFS.
"""

# Test 1: 1 x 1 board, only 'X'
board = [['X']]
Solution().solve(board)
expected = [['X']]
assert board == expected, f"Expected {expected} but got {board}"

# Test 2: 1 x 1 board, only 'O'
board = [['O']]
Solution().solve(board)
expected = [['O']]
assert board == expected, f"Expected {expected} but got {board}"

# Test 3: Board boundaries surrounded by 'O', no flip
board = [
    ['O', 'O', 'O', 'O'],
    ['O', 'X', 'X', 'O'],
    ['O', 'X', 'X', 'O'],
    ['O', 'O', 'O', 'O']
]
Solution().solve(board)
expected = [
    ['O', 'O', 'O', 'O'],
    ['O', 'X', 'X', 'O'],
    ['O', 'X', 'X', 'O'],
    ['O', 'O', 'O', 'O']
]
assert board == expected, f"Expected {expected} but got {board}"

# Test 4: Board boundaries surrounded by 'X', no flip
board = [
    ['X', 'X', 'X', 'X'],
    ['X', 'X', 'X', 'X'],
    ['X', 'X', 'X', 'X'],
    ['X', 'X', 'X', 'X']
]
Solution().solve(board)
expected = [
    ['X', 'X', 'X', 'X'],
    ['X', 'X', 'X', 'X'],
    ['X', 'X', 'X', 'X'],
    ['X', 'X', 'X', 'X']
]
assert board == expected, f"Expected {expected} but got {board}"

# Test 5: Board boundaries surrounded by 'X', flip
board = [
    ['X', 'X', 'X', 'X'],
    ['X', 'O', 'O', 'X'],
    ['X', 'O', 'O', 'X'],
    ['X', 'X', 'X', 'X']
]
Solution().solve(board)
expected = [
    ['X', 'X', 'X', 'X'],
    ['X', 'X', 'X', 'X'],
    ['X', 'X', 'X', 'X'],
    ['X', 'X', 'X', 'X']
]
assert board == expected, f"Expected {expected} but got {board}"

# Test 6: No 'O' flipped
board = [
    ['X', 'X', 'X', 'X'],
    ['O', 'O', 'O', 'X'],
    ['X', 'O', 'O', 'X'],
    ['X', 'O', 'X', 'X']
]
Solution().solve(board)
expected = [
    ['X', 'X', 'X', 'X'],
    ['O', 'O', 'O', 'X'],
    ['X', 'O', 'O', 'X'],
    ['X', 'O', 'X', 'X']
]
assert board == expected, f"Expected {expected} but got {board}"

# Test 7: 'O's flipped
board = [
    ['X', 'X', 'X', 'X'],
    ['O', 'X', 'O', 'X'],
    ['X', 'X', 'O', 'X'],
    ['X', 'O', 'X', 'O']
]
Solution().solve(board)
expected = [
    ['X', 'X', 'X', 'X'],
    ['O', 'X', 'X', 'X'],
    ['X', 'X', 'X', 'X'],
    ['X', 'O', 'X', 'O']
]
assert board == expected, f"Expected {expected} but got {board}"
