from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        def dfs(r, c, first_color):
            if not (0 <= r < len(image) and 0 <= c < len(image[r]) and image[r][c] == first_color and image[r][c] != color):
                return

            image[r][c] = color

            dfs(r + 1, c, first_color)
            dfs(r - 1, c, first_color)
            dfs(r, c + 1, first_color)
            dfs(r, c - 1, first_color)

        dfs(sr, sc, image[sr][sc])

        return image


"""
Explanation:

Start the dfs at the starting row and column index with the first color of the starting pixel. Return if the current pixel is out of bounds, not the same color as the first color, or has already been changed to the new color. Otherwise, change the current pixel to the new color and continue the dfs in all four directions. Finally, return the modified image.

Notes:

Time complexity: O(m * n), where m is the number of rows and n is the number of columns in the image.

Space complexity: O(m * n), as the method uses a call stack for the dfs function.
"""

# Test 1: Single pixel
image = [[0]]
updated_image = Solution().floodFill(image, 0, 0, 1)
assert updated_image == [[1]], f"Expected [[1]] but got {updated_image}"

# Test 2: Multiple pixels from corner
image = [[1, 1, 0], [1, 0, 1], [1, 1, 1]]
updated_image = Solution().floodFill(image, 2, 0, 2)
assert updated_image == [[2, 2, 0], [2, 0, 2], [
    2, 2, 2]], f"Expected [[2, 2, 0], [2, 0, 2], [2, 2, 2]] but got {updated_image}"

# Test 3: Multiple pixels from center
image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
updated_image = Solution().floodFill(image, 1, 1, 2)
assert updated_image == [[2, 2, 2], [2, 2, 0], [
    2, 0, 1]], f"Expected [[2, 2, 2], [2, 2, 0], [2, 0, 1]] but got {updated_image}"
