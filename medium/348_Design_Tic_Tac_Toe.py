class TicTacToe:
    def __init__(self, size=3):
        self.size = size
        self.rows = [0] * size
        self.cols = [0] * size
        self.pos_diagonal = 0
        self.neg_diagonal = 0

    def move(self, row: int, col: int, player: int):
        curr_player = 1 if player == 1 else -1

        self.rows[row] += curr_player
        self.cols[col] += curr_player

        if row == col:
            self.pos_diagonal += curr_player
        if col == self.size - row - 1:
            self.neg_diagonal += curr_player

        return self.validateMove(row, col, player)

    def validateMove(self, row: int, col: int, player: int):
        if any(abs(value) == self.size for value in (self.rows[row], self.cols[col], self.pos_diagonal, self.neg_diagonal)):
            return player

        return 0

"""
Explanation:

Initialize the game board w/ a default size of 3, and keep track of the rows, columns, and diagonals using separate arrays. The move method is used to make a move on the board, updating the relevant row, column, and diagonal values. It then calls the validateMove method to check if the move results in a win. The validateMove method checks if any of the absolute values of the row, column, and diagonal equal the board size. If any of them do, it means that the current move has resulted in a win, and it returns the player value associated with the winning move. Otherwise, it returns 0 to indicate that the move is valid but not a winning move.

Notes:

Time complexity: O(1) for all operations

Space complexity: O(n) to store the board
"""

# Test Case 1: Row win
game = TicTacToe()
game.move(0, 0, 1)
game.move(1, 0, -1)
game.move(0, 1, 1)
game.move(1, 1, -1)
result = game.move(0, 2, 1)
expected = 1
assert result == expected, f"Expected {expected} but got {result}"

# Test Case 2: Column win
game = TicTacToe()
game.move(0, 0, 1)
game.move(0, 1, -1)
game.move(1, 0, 1)
game.move(1, 1, -1)
result = game.move(2, 0, 1)
expected = 1
assert result == expected, f"Expected {expected} but got {result}"

# Test Case 3: Positive diagonal win
game = TicTacToe()
game.move(2, 0, 1)
game.move(0, 0, -1)
game.move(1, 1, 1)
game.move(0, 1, -1)
result = game.move(0, 2, 1)
expected = 1
assert result == expected, f"Expected {expected} but got {result}"

# Test Case 4: Negative diagonal win
game = TicTacToe()
game.move(0, 0, 1)
game.move(0, 1, -1)
game.move(1, 1, 1)
game.move(1, 2, -1)
result = game.move(2, 2, 1)
expected = 1
assert result == expected, f"Expected {expected} but got {result}"

# Test Case 5: Tie
game = TicTacToe()
game.move(0, 0, 1)
game.move(1, 0, -1)
game.move(0, 1, 1)
game.move(0, 2, -1)
game.move(2, 0, 1)
game.move(2, 1, -1)
game.move(2, 2, 1)
game.move(1, 1, -1)
result = game.move(1, 2, 1)
expected = 0
assert result == expected, f"Expected {expected} but got {result}"

# Test Case 6: Continue game
game = TicTacToe()
game.move(0, 0, 1)
result = game.move(0, 1, -1)
expected = 0
assert result == expected, f"Expected {expected} but got {result}"