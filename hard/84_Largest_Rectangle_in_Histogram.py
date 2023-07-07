from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []

        for i, h in enumerate(heights):
            start = i

            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index

            stack.append((start, h))

        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))

        return maxArea

"""
Explanation:

Initialize the variables `maxArea` to 0 and `stack` as an empty list. For each height in the input `heights` list: initialize the variable `start` with the current index. Enter a while loop as long as the stack is not empty and the height at the top of the stack > the current height. Pop the top element from the stack, which represents a previous height. Calculate the area of the rectangle using the popped index and height. Update maxArea with the maximum value between the current maxArea and the calculated area. Update the start variable with the popped index, as it represents the starting point of the potential rectangle. Push the updated start index and current height h onto the stack, representing a potential starting point for a new rectangle.

After the loop ends, there might be remaining elements in the stack representing unfinished rectangles. Iterate through the remaining elements in the stack. Calculate the area of the rectangle using the remaining index and height. Update maxArea with the maximum value between the current maxArea and the calculated area.

Once done, return the final maxArea as the largest rectangle area that can be formed from the given heights.

Notes:

Time complexity: O(n)

Space complexity: O(n)
"""

# Test Case 1: Heights with increasing values
heights = [1, 2, 3, 4, 5]
result = Solution().largestRectangleArea(heights)
expected = 9
assert result == expected, f"Expected {expected} but got {result}"

# Test Case 2: Heights with decreasing values
heights = [5, 4, 3, 2, 1]
result = Solution().largestRectangleArea(heights)
expected = 9
assert result == expected, f"Expected {expected} but got {result}"

# Test Case 3: Heights with alternating values
heights = [1, 5, 2, 4, 3]
result = Solution().largestRectangleArea(heights)
expected = 8
assert result == expected, f"Expected {expected} but got {result}"

# Test Case 4: Heights with equal values
heights = [3, 3, 3, 3, 3]
result = Solution().largestRectangleArea(heights)
expected = 15
assert result == expected, f"Expected {expected} but got {result}"

# Test Case 5: Heights with random values
heights = [2, 1, 5, 6, 2, 3]
result = Solution().largestRectangleArea(heights)
expected = 10
assert result == expected, f"Expected {expected} but got {result}"
