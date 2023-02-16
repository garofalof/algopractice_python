from collections import defaultdict
from typing import List


class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph = defaultdict(list)

        for i in range(n):
            m = manager[i]

            if m >= 0:
                graph[m].append(i)

        stack = [(headID, 0)]
        result = 0

        while stack:
            emp, time = stack.pop()
            time += informTime[emp]
            result = max(time, result)

            if emp in graph:
                for report in graph[emp]:
                    stack.append((report, time))

        return result

"""
Explanation:

Build a graph from the manager list, where each employee's manager is a node with its direct reports as edges. Traverse the graph using a stack to keep track of the current employee and their accumulated time. Start with the head of the organization and 0 accumulated time. Pop an employee and their accumulated time from the stack. Update the maximum accumulated time seen so far. If the employee has direct reports, add each report and their accumulated time to the stack. Repeat until the stack is empty. Finally, return the maximum accumulated time seen so far.

Notes:

Time Complexity: O(n), where n is the number of employees in the organization.

Space Complexity: O(n), where n is the number of employees in the organization. This is due to the use of the stack and the graph to represent the organizational hierarchy.
"""

# Test 1: Single employee w/ no subordinates
n = 1
headID = 0
manager = [-1]
informTime = [0]
totalTime = Solution().numOfMinutes(n, headID, manager, informTime)
expected = 0
assert totalTime == expected, f"Expected {expected} but got {totalTime}"

# Test 2: Multiple employees w/ no subordinates
n = 5
headID = 0
manager = [-1, -1, -1, -1, -1]
informTime = [1, 1, 1, 1, 1]
totalTime = Solution().numOfMinutes(n, headID, manager, informTime)
expected = 1
assert totalTime == expected, f"Expected {expected} but got {totalTime}"

# Test 3: Single level hierarchy
n = 4
headID = 0
manager = [-1, 0, 0, 0]
informTime = [1, 0, 0, 0]
totalTime = Solution().numOfMinutes(n, headID, manager, informTime)
expected = 1
assert totalTime == expected, f"Expected {expected} but got {totalTime}"

# Test 4: Two level hierarchy
n = 4
headID = 0
manager = [-1, 0, 1, 1]
informTime = [1, 2, 0, 0]
totalTime = Solution().numOfMinutes(n, headID, manager, informTime)
expected = 3
assert totalTime == expected, f"Expected {expected} but got {totalTime}"

# Test 5: Multiple subordinates w/ different times
n = 6
headID = 0
manager = [-1, 0, 0, 1, 2, 2]
informTime = [0, 3, 5, 7, 2, 4]
totalTime = Solution().numOfMinutes(n, headID, manager, informTime)
expected = 10
assert totalTime == expected, f"Expected {expected} but got {totalTime}"
