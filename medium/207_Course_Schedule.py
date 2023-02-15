from collections import defaultdict
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        visiting = set()
        visited = set()

        for course, prereq in prerequisites:
            graph[course].append(prereq)

        for course in list(graph.keys()):
            if self.dfs(course, graph, visiting, visited):
                return False

        return True

    def dfs(self, course, graph, visiting, visited):
        visiting.add(course)

        for prereq in graph[course]:
            if prereq in visited:
                continue
            if prereq in visiting or self.dfs(prereq, graph, visiting, visited):
                return True

        visiting.remove(course)
        visited.add(course)
        return False


"""
Explanation:

Create a dictionary "graph" with the course numbers as keys and the list of prerequisites as values. Use two sets "visiting" and "visited" to keep track of the nodes being visited in the graph.

Iterate over the graph keys and call the dfs function to check if there is a cycle in the graph. In the dfs function, add the course to the "visiting" set. For each prereq of the course, if the prereq is in the "visited" set, continue. If the prereq is in the "visiting" set, then there is a cycle in the graph, return True. Otherwise, recursively call the dfs function with the prereq as the course. If any call to dfs returns True, then there is a cycle in the graph, return True. When all prereqs have been visited for the current course, remove it from the "visiting" set and add it to the "visited" set. Finally, return False to indicate that there is no cycle in the graph.

Notes:

- Time complexity: O(V + E), where V is the number of vertices and E is the number of edges in the graph.
- Space complexity: O(V + E), where V is the number of vertices and E is the number of edges in the graph.
"""

# Test 1: Single course, no prereqs
n = 1
prereqs = []
can_finish = Solution().canFinish(n, prereqs)
expected = True
assert can_finish == expected, f"Expected {expected} but got {can_finish}"

# Test 2: Single course, single prereq
n = 1
prereqs = [[0, 0]]
can_finish = Solution().canFinish(n, prereqs)
expected = False
assert can_finish == expected, f"Expected {expected} but got {can_finish}"

# Test 3: Multiple courses, no cycles
n = 3
prereqs = [[0, 1], [0, 2], [1, 2]]
can_finish = Solution().canFinish(n, prereqs)
expected = True
assert can_finish == expected, f"Expected {expected} but got {can_finish}"

# Test 4: Multiple courses with cycle
n = 3
prereqs = [[0, 1], [1, 2], [2, 0]]
can_finish = Solution().canFinish(n, prereqs)
expected = False
assert can_finish == expected, f"Expected {expected} but got {can_finish}"

# Test 5: Multiple courses with same prereq
n = 4
prereqs = [[0, 1], [2, 1], [3, 1]]
can_finish = Solution().canFinish(n, prereqs)
expected = True
assert can_finish == expected, f"Expected {expected} but got {can_finish}"
