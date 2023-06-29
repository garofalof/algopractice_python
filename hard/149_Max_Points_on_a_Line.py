from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        max_count = 0

        def find_slope(p1, p2):
            x1, y1 = p1
            x2, y2 = p2

            if y1 - y2 == 0:
                slope = 0
            else:
                slope = "undefined" if x1 - x2 == 0 else (x1 - x2) / (y1 - y2)

            return slope

        for i in range(len(points)):
            slope_count = {}

            for j in range(i + 1, len(points)):
                point1 = points[i]
                point2 = points[j]
                slope = find_slope(point1, point2)

                slope_count[slope] = slope_count.get(slope, 0) + 1
                max_count = max(max_count, slope_count[slope])

        return max_count + 1

"""
Explanation:

Iterate through each point and compare it with all other points to calculate the slopes of the lines formed by pairs of points. Use a dictionary slope_count to keep track of the count of each slope encountered. The max count is updated whenever a new slope count exceeds the current maximum. The helper function find_slope calculates the slope between two points (x1, y1) and (x2, y2). It handles special cases where the y-coordinates are equal (horizontal line) or the x-coordinates are equal (vertical line), and returns the slope value accordingly.

Finally, return the max count once we're done iterating through all points.

Notes:

Time complexity: O(n^2), as the nested loop iterates through each pair of points for each point

Space complexity: O(n) to store the slope counts
"""

# Test Case 1: Normal case w/ 3 points
points = [[1, 1], [2, 2], [3, 3]]
result = Solution().maxPoints(points)
expected = 3
assert result == expected, f"Expected {expected} but got {result}"

# Test Case 2: All points are on the same line
points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]
result = Solution().maxPoints(points)
expected = 5
assert result == expected, f"Expected {expected} but got {result}"

# Test Case 3: Points form a triangle
points = [[1, 1], [2, 2], [3, 3], [1, 3], [2, 1]]
result = Solution().maxPoints(points)
expected = 3
assert result == expected, f"Expected {expected} but got {result}"

# Test Case 4: Points form a vertical line
points = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5]]
result = Solution().maxPoints(points)
expected = 5
assert result == expected, f"Expected {expected} but got {result}"

# Test Case 5: Points form a horizontal line
points = [[1, 1], [2, 1], [3, 1], [4, 1], [5, 1]]
result = Solution().maxPoints(points)
expected = 5
assert result == expected, f"Expected {expected} but got {result}"

# Test Case 6: Single point
points = [[1, 1]]
result = Solution().maxPoints(points)
expected = 1
assert result == expected, f"Expected {expected} but got {result}"

# Test Case 7: Single slope between points
points = [[1, 0], [2, 3], [3, 5]]
result = Solution().maxPoints(points)
expected = 2
assert result == expected, f"Expected {expected} but got {result}"