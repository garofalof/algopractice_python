from typing import List


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        dist = [float('inf')] * n
        dist[0] = 0

        cost = 0
        curr_point = 0

        for _ in range(n - 1):
            min_dist = float('inf')
            next_point = -1

            for i in range(n):
                if dist[i] > 0:
                    x1, y1 = points[curr_point]
                    x2, y2 = points[i]
                    curr_dist = abs(x1 - x2) + abs(y1 - y2)
                    dist[i] = min(dist[i], curr_dist)

                    if dist[i] < min_dist:
                        min_dist = dist[i]
                        next_point = i

            cost += min_dist
            dist[next_point] = 0
            curr_point = next_point

        return cost


"""
Explanation:

First, initialize the cost to 0, the next point to be considered to 0, the number of points to n, and the distance array dist to a list of n values initialized to infinity, with the first element set to 0.

Then, for each point from 1 to n - 1, we find the minimum distance to the next point. We do this by looping through all the points from 1 to n - 1 and updating the distance array dist for each point if the current distance < the stored distance. If the current distance < the minimum distance found so far, we update the minimum distance and the next point to be considered.

At each iteration of the outer loop, we add the minimum distance found to the total cost and set the distance of the next point to 0, indicating that it has been visited. We repeat this process until all points have been visited. Once done, we return the final cost.

Notes:

Time complexity: O(n^2), where n is the number of points.
Space complexity: O(n), where n is the number of points for the distance array.
"""

# Test 1: Single point
points = [[0, 1]]
min_cost = Solution().minCostConnectPoints(points)
expected = 0
assert min_cost == expected, f"Expected {expected} but got {min_cost}"

# Test 2: Two points
points = [[0, 1], [4, 2]]
min_cost = Solution().minCostConnectPoints(points)
expected = 5
assert min_cost == expected, f"Expected {expected} but got {min_cost}"

# Test 3: Points in square
points = [[0, 0], [4, 0], [4, 4], [0, 4]]
min_cost = Solution().minCostConnectPoints(points)
expected = 12
assert min_cost == expected, f"Expected {expected} but got {min_cost}"

# Test 4: Points in line
points = [[0, 0], [1, 1], [2, 2], [3, 3]]
min_cost = Solution().minCostConnectPoints(points)
expected = 6
assert min_cost == expected, f"Expected {expected} but got {min_cost}"

# Test 5: Points randomized
points = [[-1, 2], [3, 0], [1, 2], [5, 7], [-3, 4], [2, 5]]
min_cost = Solution().minCostConnectPoints(points)
expected = 19
assert min_cost == expected, f"Expected {expected} but got {min_cost}"
