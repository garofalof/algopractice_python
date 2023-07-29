from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            rowCheck = set()
            colCheck = set()
            boxCheck = set()

            for j in range(len(board[0])):
                row = board[i][j]
                col = board[j][i]
                boxRow = 3 * (i // 3) + (j // 3)
                boxCol = 3 * (i % 3) + (j % 3)
                box = board[boxRow][boxCol]

                if row != ".":
                    if row in rowCheck:
                        return False
                    rowCheck.add(row)
                if col != ".":
                    if col in colCheck:
                        return False
                    colCheck.add(col)
                if box != ".":
                    if box in boxCheck:
                        return False
                    boxCheck.add(box)

        return True


"""
Explanation:

To determine if a given Sudoku board is valid, we need to check three conditions: rows, columns, and 3x3 boxes. Iterate through the board, maintaining three sets for each row, column, and 3x3 box to check for duplicates. For each row, use the set "rowCheck" to store the encountered digits. Similarly, for each column, use "colCheck," and for each 3x3 box, use "boxCheck." The 3x3 box is determined based on the current row and column index. Iterate through the board, checking each cell's value. If it contains a digit, check whether that digit is already present in the corresponding "rowCheck," "colCheck," or "boxCheck" set. If the digit is already present, we have a duplicate and the Sudoku board is invalid. If we finish the iteration without finding any duplicates, it means the Sudoku board is valid, and the function returns True.

Notes:

Time complexity: O(1), as the board is a fixed size

Space complexity: O(1), as we store max 9 unique digits for each set
"""

# Test Case 1: Empty board
board = [['.'] * 9 for _ in range(9)]
result = Solution().isValidSudoku(board)
expected = True
assert result == expected, f"Expected {expected} but got {result}"

# Test Case 2: Valid board
board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]
result = Solution().isValidSudoku(board)
expected = True
assert result == expected, f"Expected {expected} but got {result}"

# Test Case 3: Invalid board, row failure
board = [
    ["5", "3", "5", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]
result = Solution().isValidSudoku(board)
expected = False
assert result == expected, f"Expected {expected} but got {result}"
