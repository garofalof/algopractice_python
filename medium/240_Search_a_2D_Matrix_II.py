from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col = len(matrix) - 1, 0

        while row >= 0 and col < len(matrix[0]):
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                col += 1
            else:
                row -= 1
        return False


"""
Explanation:

Start at the bottom-left corner of the matrix, which is the only position where all the elements to the right are greater and all the elements above are smaller. Compare the target with the current element. If the current element == target, return True. If the current element < target, move to the right by incrementing the column index. If the current element > target, move up by decrementing the row index. Keep moving to the right or up until we either find the target or hit the edge of the matrix. If we hit the edge without finding target, we exit the loop and return False.

Notes:

Time Complexity: O(m + n), where m and n are the number of rows and columns in the matrix.

Space Complexity: O(1), since we only use a constant amount of extra space for the row and column indices.
"""

# Test 1: Single element, match
matrix = [[10]]
target = 10
target_found = Solution().searchMatrix(matrix, target)
expected = True
assert target_found == expected, f"Expected {expected} but got {target_found}"

# Test 2: Single element, no match
matrix = [[10]]
target = 1
target_found = Solution().searchMatrix(matrix, target)
expected = False
assert target_found == expected, f"Expected {expected} but got {target_found}"

# Test 3: Multiple elements, match in first row
matrix = [[1, 7, 10], [6, 9, 12], [14, 21, 32]]
target = 7
target_found = Solution().searchMatrix(matrix, target)
expected = True
assert target_found == expected, f"Expected {expected} but got {target_found}"

# Test 4: Multiple elements, match in last row
matrix = [[1, 7, 10], [6, 9, 12], [14, 21, 32]]
target = 21
target_found = Solution().searchMatrix(matrix, target)
expected = True
assert target_found == expected, f"Expected {expected} but got {target_found}"

# Test 5: Multiple elements, match in first col
matrix = [[1, 7, 10], [6, 9, 12], [14, 21, 32]]
target = 6
target_found = Solution().searchMatrix(matrix, target)
expected = True
assert target_found == expected, f"Expected {expected} but got {target_found}"

# Test 6: Multiple elements, match in last col
matrix = [[1, 7, 10], [6, 9, 12], [14, 21, 32]]
target = 12
target_found = Solution().searchMatrix(matrix, target)
expected = True
assert target_found == expected, f"Expected {expected} but got {target_found}"

# Test 7: Multiple elements, match in middle
matrix = [[1, 7, 10], [6, 9, 12], [14, 21, 32]]
target = 9
target_found = Solution().searchMatrix(matrix, target)
expected = True
assert target_found == expected, f"Expected {expected} but got {target_found}"

# Test 8: Multiple elements, no match
matrix = [[1, 7, 10], [6, 9, 12], [14, 21, 32]]
target = 50
target_found = Solution().searchMatrix(matrix, target)
expected = False
assert target_found == expected, f"Expected {expected} but got {target_found}"
