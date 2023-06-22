import collections


class Solution:
    def racecar(self, target: int) -> int:
        q = collections.deque()
        q.append((0, 1, 0))
        visited = set()

        while q:
            pos, speed, moves = q.popleft()
            key = f'{pos},{speed}'

            if pos == target:
                return moves
            if key in visited:
                continue

            visited.add(key)

            q.append((pos + speed, speed * 2, moves + 1))

            if (pos + speed > target and speed > 0) or (pos + speed < target and speed < 0):
                speed = 1 if speed < 0 else -1
                q.append((pos, speed, moves + 1))

        return -1

"""
Explanation:

Initialize a queue to store the positions, speeds, and move counts as tuples. Enqueue the initial position of 0 with initial speed 1 and 0 moves. Initialize a set to store visited positions. Perform a BFS on the possible positions. In BFS: dequeue a position from the front of the queue. Check if the current position is equal to the target position. If it is, return the number of moves. Generate a unique key for the current position by combining the position and speed. If the key is already in the visited set, skip to the next iteration of the loop. Add the key to the visited set. Enqueue 2 possible moves: move to the next position with the speed doubled and increase the move count by 1. If the next position > target and accelerating or < target and decelerating, add a move w/ curr position, speed set to 1 if decelerating or -1 if accelerating, and moves increased by 1.

If the loop completes without finding the target position, return -1 to indicate that it is not reachable.

Notes:

Time complexity: O(t * log t), as in the worst case, the algorithm explores positions up to the target position T, and for each position, it generates two possible moves. The logarithmic factor arises from the fact that speed doubles at each iteration.

Space complexity: O(t * log t), as the size of the queue is directly correlated to the number of moves we need to make to reach our target.
"""

# Test Case 1: Target is minimum of position 1
target = 1
result = Solution().racecar(target)
expected = 1
assert result == expected, f"Expected {expected} but got {result}"

# Test Case 2: Target is maximum of position 10^4
target = 10**4
result = Solution().racecar(target)
expected = 45
assert result == expected, f"Expected {expected} but got {result}"

# Test Case 3: Target is small positive number
target = 3
result = Solution().racecar(target)
expected = 2
assert result == expected, f"Expected {expected} but got {result}"

# Test Case 4: Target is large positive number
target = 5000
result = Solution().racecar(target)
expected = 41
assert result == expected, f"Expected {expected} but got {result}"