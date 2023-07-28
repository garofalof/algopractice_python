from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left, right, top, bottom = 0, len(matrix[0]) - 1, 0, len(matrix) - 1
        result = []

        while left <= right and top <= bottom:
            for i in range(left, right + 1):
                result.append(matrix[top][i])
            top += 1

            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1

            if top <= bottom:
                for i in range(right, left - 1,  -1):
                    result.append(matrix[bottom][i])
                bottom -= 1

            if left <= right:
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1

        return result


"""
Explanation:

Store left, right, top, and bottom boundaries. Initialize empty result list to store spiral order. Use while loop to traverse matrix in spiral order. While left <= right and top <= bottom: add left to right nodes from top boundary and increase top by 1. Add top to bottom nodes from right boundary and decrease right by 1. If top <= bottom, add nodes right to left from bottom boundary. If left <= right, add bottom to top nodes from left boundary.

Once done iterating through matrix, return result.

Notes:

Time complexity: O(m * n), where m is the number of rows and n is the number of columns

Space complexity: O(m * n) to store nodes
"""

# Test Case 1: 1 x 1
matrix = [[1]]
result = Solution().spiralOrder(matrix)
expected = [1]
assert result == expected, f"Expected {expected} but got {result}"

# Test Case 2: 2 x 2
matrix = [[1, 2], [3, 4]]
result = Solution().spiralOrder(matrix)
expected = [1, 2, 4, 3]
assert result == expected, f"Expected {expected} but got {result}"

# Test Case 3: 3 x 3
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
result = Solution().spiralOrder(matrix)
expected = [1, 2, 3, 6, 9, 8, 7, 4, 5]
assert result == expected, f"Expected {expected} but got {result}"

# Test Case 4: 3 x 5
matrix = [
    [1, 2, 3, 4, 5],
    [12, 13, 14, 15, 6],
    [11, 10, 9, 8, 7]
]
result = Solution().spiralOrder(matrix)
expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
assert result == expected, f"Expected {expected} but got {result}"

# Test Case 5: Single column
matrix = [
    [1],
    [2],
    [3],
    [4],
    [5]
]
result = Solution().spiralOrder(matrix)
expected = [1, 2, 3, 4, 5]
assert result == expected, f"Expected {expected} but got {result}"

# Test Case 6: Single row
matrix = [[1, 2, 3, 4, 5]]
result = Solution().spiralOrder(matrix)
expected = [1, 2, 3, 4, 5]
assert result == expected, f"Expected {expected} but got {result}"
