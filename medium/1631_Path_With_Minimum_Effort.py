from typing import List
import heapq


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        heap = []
        visited = set()

        heapq.heappush(heap, (0, 0, 0))

        directions = [
            (1, 0),
            (0, 1),
            (-1, 0),
            (0, -1)
        ]

        rows, cols = len(heights), len(heights[0])

        while heap:
            diff, row, col = heapq.heappop(heap)
            curr_height = heights[row][col]

            if row == rows - 1 and col == cols - 1:
                return diff

            key = (row, col)

            if key in visited:
                continue

            visited.add(key)

            for r, c in directions:
                newR, newC = row + r, col + c

                if newR < 0 or newC < 0 or newR >= rows or newC >= cols:
                    continue

                new_height = heights[newR][newC]
                new_diff = abs(curr_height - new_height)
                heapq.heappush(heap, (max(new_diff, diff), newR, newC))


"""
Explanation:

To solve this problem, use Dijkstra's algorithm, which is a graph search algorithm that finds the shortest path between nodes in a graph. In this case, the graph is the grid of heights, where each cell is a node and the edges between cells are weighted by the absolute difference in height between the two cells.

Use a heap to keep track of the nodes to be visited, where the priority of each node is the minimum effort required to reach that node. Start at the top-left corner of the grid and explore the graph in a breadth-first manner, using the heap to select the next node to visit based on the minimum effort required to reach the node. Maintain a set of visited nodes to avoid revisiting nodes that have already been explored. Terminate when we reach the bottom-right corner of the grid by returning the minimum effort.

Notes:

Time complexity: O(m * n (log m * n)), where m and n are the dimensions of the input grid. The algorithm visits each node in the grid at most once, and each visit involves a heap operation, which takes O(log m * n) time.

Space complexity: O(m * n), where m and n are the dimensions of the input grid. The algorithm maintains a priority queue of at most m * n nodes and a set of visited nodes of at most m * n nodes.
"""

# Test 1: Single node == 1
heights = [[1]]
min_effort = Solution().minimumEffortPath(heights)
expected = 0
assert min_effort == expected, f"Expected {expected} but got {min_effort}"

# Test 2: Single node == 10 ** 6 (max value)
heights = [[10 ** 6]]
min_effort = Solution().minimumEffortPath(heights)
expected = 0
assert min_effort == expected, f"Expected {expected} but got {min_effort}"

# Test 3: 1 x 2 matrix large diff
heights = [[1], [10 ** 6]]
min_effort = Solution().minimumEffortPath(heights)
expected = 999999
assert min_effort == expected, f"Expected {expected} but got {min_effort}"

# Test 4: 2 x 1 matrix large diff
heights = [[1, 10 ** 6]]
min_effort = Solution().minimumEffortPath(heights)
expected = 999999
assert min_effort == expected, f"Expected {expected} but got {min_effort}"

# Test 5: 2 x 2 matrix large diff
heights = [[1, 10 ** 6], [10 ** 6, 1]]
min_effort = Solution().minimumEffortPath(heights)
expected = 999999
assert min_effort == expected, f"Expected {expected} but got {min_effort}"

# Test 7: 3 x 3 down and right
heights = [[1, 2, 2], [3, 8, 2], [5, 3, 5]]
min_effort = Solution().minimumEffortPath(heights)
expected = 2
assert min_effort == expected, f"Expected {expected} but got {min_effort}"

# Test 8: 3 x 3 right and down
heights = [[1, 2, 3], [3, 8, 4], [5, 3, 5]]
min_effort = Solution().minimumEffortPath(heights)
expected = 1
assert min_effort == expected, f"Expected {expected} but got {min_effort}"
