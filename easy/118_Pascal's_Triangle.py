from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1]]

        for i in range(1, numRows):
            prev = result[-1]
            curr = [0] * (i + 1)

            for j in range(len(curr)):
                curr[j] = (prev[j] if j < len(prev) else 0) + \
                    (prev[j - 1] if j > 0 else 0)

            result.append(curr)

        return result


"""
Explanation:

Start by creating a 2D list containing the first row of the triangle, which is always [1]. Then iterate over the remaining rows, starting with the second row. For each row, create a new list curr with i+1 elements, where i is the index of the current row. Then iterate over the indices of curr, and for each index j, calculate the value of curr[j] by adding the values of the corresponding indices in the previous row prev (or 0 if the index is out of bounds).

After calculating all the values of curr, append it to the result list, and move on to the next row. Finally, return the 2D list containing all the rows of the Pascal's triangle.

Notes:

Time complexity: O(n ^ 2), where n is the number of rows.

Space complexity: O(1), as we don't count the output array as extra space.
"""

# Test 1: Single row
n = 1
triangle = Solution().generate(n)
expected = [[1]]
assert triangle == expected, f"Expected {expected} but got {triangle}"

# Test 2: Even number of rows
n = 4
triangle = Solution().generate(n)
expected = [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]
assert triangle == expected, f"Expected {expected} but got {triangle}"

# Test 3: Odd number of rows
n = 5
triangle = Solution().generate(n)
expected = [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
assert triangle == expected, f"Expected {expected} but got {triangle}"
