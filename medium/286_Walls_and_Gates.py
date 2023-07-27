import collections
from typing import List


class Solution:
    def walls_and_gates(self, rooms: List[List[int]]):
        last_row, last_col = len(rooms) - 1, len(rooms[0]) - 1
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        q = collections.deque()

        for r in range(last_row + 1):
            for c in range(last_col + 1):
                if rooms[r][c] == 0:
                    q.append((r, c))
        while q:
            r, c = q.popleft()

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc

                if 0 <= nr <= last_row and 0 <= nc <= last_col and rooms[nr][nc] == pow(2, 31) - 1:
                    rooms[nr][nc] = rooms[r][c] + 1
                    q.append((nr, nc))

        return rooms


"""
Explanation:

Initialize a queue and iterate through rooms to add all gate coordinates to the queue. Then perform BFS, starting from each gate and propagating to all reachable empty rooms in the grid. At each iteration, search adjacent cells for empty rooms, update the empty room's distance at current node + 1, and append the empty room coordinates to the queue.

Once done, return rooms grid containing the distances from each gate to empty rooms.

Notes:

Time complexity: O(m * n), as we traverse the grid at most twice

Space complexity: O(m * n) to store coordinates in the queue
"""

# Test Case 1: One gate and one empty room
solution = Solution()
rooms = [
    [pow(2, 31) - 1, -1],
    [0, -1],
]
result = Solution().walls_and_gates(rooms)
expected = [
    [1, -1],
    [0, -1],
]
assert result == expected, f"Expected {expected} but got {result}"

# Test Case 2: Multiple gates and empty rooms
solution = Solution()
rooms = [
    [pow(2, 31) - 1, -1, 0],
    [pow(2, 31) - 1, -1, pow(2, 31) - 1],
    [pow(2, 31) - 1, pow(2, 31) - 1, pow(2, 31) - 1],
]
result = Solution().walls_and_gates(rooms)
expected = [[6, -1, 0], [5, -1, 1], [4, 3, 2]]
assert result == expected, f"Expected {expected} but got {result}"

# Test Case 3: Walls only
solution = Solution()
rooms = [
    [-1, -1, -1],
    [-1, -1, -1],
]
result = Solution().walls_and_gates(rooms)
expected = [[-1, -1, -1], [-1, -1, -1]]
assert result == expected, f"Expected {expected} but got {result}"

# Test Case 4: Gates only
rooms = [
    [0, 0, 0],
    [0, 0, 0],
]
result = Solution().walls_and_gates(rooms)
expected = [
    [0, 0, 0],
    [0, 0, 0],
]
assert result == expected, f"Expected {expected} but got {result}"

# Test Case 5: Unreachable empty rooms
rooms = [
    [0, -1, pow(2, 31) - 1],
    [0, -1, -1],
    [0, pow(2, 31) - 1, 0],
]
result = Solution().walls_and_gates(rooms)
expected = [[0, -1, 2147483647], [0, -1, -1], [0, 1, 0]]
assert result == expected, f"Expected {expected} but got {result}"
