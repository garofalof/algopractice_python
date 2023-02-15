from collections import defaultdict
from math import inf
from typing import List


class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        point_map = defaultdict(set)
        min_area = float(inf)

        for x, y in points:
            point_map[x].add(y)
        for x1, y1 in points:
            for x2, y2 in points:
                sameCross = x1 == x2 or y1 == y2

                if not sameCross and y2 in point_map[x1] and y1 in point_map[x2]:
                    area = abs(x1 - x2) * abs(y1 - y2)
                    min_area = min(min_area, area)

        return 0 if min_area == float(inf) else min_area


"""
Explanation:

Use a dictionary to store the y-coordinates of all the points having a particular x-coordinate. Next, use 2 nested loops to find pairs of points (x1, y1) and (x2, y2) and check if they are forming a rectangle. If a rectangle is found, calculate the area formed by the four points and update the minimum area found so far. Finally, return the minimum area of the rectangle found. If no rectangle is found, then return zero.

Notes:

Time complexity: The solution uses two nested loops to find pairs of points, so the time complexity is O(n^2), where n is the number of points in the input list.

Space complexity: The solution uses a defaultdict to store the y-coordinates of all the points having a particular x-coordinate, so the space complexity is O(n), where n is the number of points in the input list.
"""

# Test 1: Single point
points = [[0, 0]]
min_area = Solution().minAreaRect(points)
expected = 0
assert min_area == expected, f"Expected {expected} but got {min_area}"

# Test 2: Multiple points no rectangle
points = [[0, 0], [1, 0], [3, 0], [5, 1]]
min_area = Solution().minAreaRect(points)
expected = 0
assert min_area == expected, f"Expected {expected} but got {min_area}"

# Test 3: Multiple points one rectangle
points = [[0, 0], [0, 3], [3, 0], [3, 3]]
min_area = Solution().minAreaRect(points)
expected = 9
assert min_area == expected, f"Expected {expected} but got {min_area}"

# Test 4: Multiple points multiple rectangles
points = [[0, 0], [0, 3], [3, 0], [3, 3], [0, 5], [5, 0], [5, 5]]
min_area = Solution().minAreaRect(points)
expected = 9
assert min_area == expected, f"Expected {expected} but got {min_area}"
