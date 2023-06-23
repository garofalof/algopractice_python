from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        negDiagonals = set()
        posDiagonals = set()
        board = [["." for _ in range(n)] for _ in range(n)]
        result = []

        def backtrack(row):
            if row == n:
                result.append(["".join(row) for row in board])
                return

            for col in range(n):
                posDiagonal = row + col
                negDiagonal = row - col

                if (
                    col in cols
                    or posDiagonal in posDiagonals
                    or negDiagonal in negDiagonals
                ):
                    continue

                cols.add(col)
                posDiagonals.add(posDiagonal)
                negDiagonals.add(negDiagonal)

                board[row][col] = "Q"
                backtrack(row + 1)

                cols.remove(col)
                posDiagonals.remove(posDiagonal)
                negDiagonals.remove(negDiagonal)
                board[row][col] = "."

        backtrack(0)
        return result


"""
Explanation:

Initialize sets tracking placed columns and diagonals. Build an n x n board and set result board to empty list. Backtrack on board starting on row 0. Inside backtrack, check if the current row is equal to n. If so, a valid solution has been found and we add to result. We then return to exit and continue exploring all other possibilities.

If the current row is not equal to n, the algorithm proceeds with the placement of a queen in each column of the current row that satisfies the constraints. For each column, check if the current column, the positive diagonal, and the negative diagonal are already occupied by queens. If any of these positions are already occupied, skip the current column and continue with the next iteration.

If the current column satisfies the constraints, the algorithm updates the sets by adding the corresponding positions of the queen. It then places the queen on the board at the current row and column. After placing the queen, we make a recursive call to `backtrack` with the next row to explore the next row.

Once all possibilities are explored, the `backtrack` function backtracks by removing the queen from the board and updating the sets accordingly by removing the corresponding positions.

Finally, the function returns the result list, which contains all valid solutions.

Notes:

Time complexity: O(n!), as we have n tries on the first row, n - 1 tries on the second row, and so on

Space complexity: O(n ^ 2) to keep board state
"""

# Test Case 1: n == 1
n = 1
result = Solution().solveNQueens(n)
expected = [['Q']]
assert result == expected, f'Expected {expected} but got {result}'

# Test Case 2: n == 2
n = 2
result = Solution().solveNQueens(n)
expected = []
assert result == expected, f'Expected {expected} but got {result}'

# Test Case 3: n == 3
n = 3
result = Solution().solveNQueens(n)
expected = []
assert result == expected, f'Expected {expected} but got {result}'

# Test Case 4: n == 4
n = 4
result = Solution().solveNQueens(n)
expected = [['.Q..', '...Q', 'Q...', '..Q.'], ['..Q.', 'Q...', '...Q', '.Q..']]
assert result == expected, f'Expected {expected} but got {result}'

# Test Case 5: n == 5
n = 5
result = Solution().solveNQueens(n)
expected = [['Q....', '..Q..', '....Q', '.Q...', '...Q.'], ['Q....', '...Q.', '.Q...', '....Q', '..Q..'], ['.Q...', '...Q.', 'Q....', '..Q..', '....Q'], ['.Q...', '....Q', '..Q..', 'Q....', '...Q.'], ['..Q..', 'Q....', '...Q.', '.Q...', '....Q'], [
    '..Q..', '....Q', '.Q...', '...Q.', 'Q....'], ['...Q.', 'Q....', '..Q..', '....Q', '.Q...'], ['...Q.', '.Q...', '....Q', '..Q..', 'Q....'], ['....Q', '.Q...', '...Q.', 'Q....', '..Q..'], ['....Q', '..Q..', 'Q....', '...Q.', '.Q...']]
assert result == expected, f'Expected {expected} but got {result}'
