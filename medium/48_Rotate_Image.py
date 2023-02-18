from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        l, r = 0, len(matrix[0]) - 1

        while l < r:
            window = r - l

            for i in range(window):
                t, b = l, r

                topLeft = matrix[t][l + i]
                matrix[t][l + i] = matrix[b - i][l]
                matrix[b - i][l] = matrix[b][r - i]
                matrix[b][r - i] = matrix[t + i][r]
                matrix[t + i][r] = topLeft

            l += 1
            r -= 1


"""
Explanation:

For each layer in the matrix, swap the values of four elements in the matrix in a cyclical fashion. Start with the top left element, move clockwise to the top right element, then to the bottom right element, and finally to the bottom left element. Repeat this process for each layer, stopping when we reach the center of the matrix.

Notes:

Time complexity: O(n^2), where n is the length of one side of the input matrix. We need to visit every element in the matrix once.

Space complexity: O(1), since we are modifying the input matrix in-place and not using any extra data structures.
"""

# Test 1: n == 1
n = [[1]]
Solution().rotate(n)
expected = [[1]]
assert n == expected, f"Expected {expected} but got {n}"

# Test 2: n == 2
n = [[1, 2], [3, 4]]
Solution().rotate(n)
expected = [[3, 1], [4, 2]]
assert n == expected, f"Expected {expected} but got {n}"

# Test 3: n == odd
n = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
Solution().rotate(n)
expected = [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
assert n == expected, f"Expected {expected} but got {n}"

# Test 4: n == even
n = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
Solution().rotate(n)
expected = [[13, 9, 5, 1], [14, 10, 6, 2], [15, 11, 7, 3], [16, 12, 8, 4]]
assert n == expected, f"Expected {expected} but got {n}"
