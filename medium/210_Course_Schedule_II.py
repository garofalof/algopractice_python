from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {i: [] for i in range(numCourses)}
        visiting = set()
        visited = set()
        result = []

        def dfs(node):
            if node in visiting:
                return False
            if node in visited:
                return True

            visiting.add(node)
            prereqs = graph.get(node)

            if prereqs:
                for course in prereqs:
                    if not dfs(course):
                        return False

            visiting.remove(node)
            visited.add(node)
            result.append(node)

            return True

        for course, prereq in prerequisites:
            graph[course].append(prereq)
        for course in graph:
            if not dfs(course):
                return []

        return result


"""
Explanation:

Initialize a dictionary called graph that will hold the prerequisites as keys and the courses as values. Create two sets, visiting and visited, and an empty list, result, to keep track of the visited courses and their order. Initialize the graph dictionary with keys 0 to numCourses - 1 and values as empty lists. For each prerequisite, append the course to its prerequisite list in the graph dictionary.

For each course in the graph dictionary, call the dfs function. If dfs returns False, then a cycle has been found, and we return an empty list.

The dfs function takes in a course as an argument. If the course is already in the visiting set, then a cycle has been found, and we return False. If the course has already been visited, we return True. Add the course to the visiting set, get its prerequisites from the graph dictionary, and for each prerequisite, recursively call the dfs function. If the dfs function returns False for any of the prerequisites, then there is a cycle, and we return False. Once all prerequisites have been visited, remove the course from the visiting set, add it to the visited set, and append it to the result list. Finally, return True.

If we successfully traverse all courses without finding a cycle, return the result list containing the courses in the order in which they should be taken.

Notes:

Time complexity: O(N + E), where N is the number of courses and E is the number of prerequisites, as we traverse each course and prerequisite once in the graph.

Space complexity: O(N + E), as we store the graph as a dictionary and sets, and the result list can hold up to N courses.
"""

# Test 1: Num courses == 1, no prereqs
n = 1
prereqs = []
course_order = Solution().findOrder(n, prereqs)
expected = [0]
assert course_order == expected, f"Expected {expected} but got {course_order}"

# Test 2: Num courses == 2, no prereqs
n = 2
prereqs = []
course_order = Solution().findOrder(n, prereqs)
expected = [0, 1]
assert course_order == expected, f"Expected {expected} but got {course_order}"

# Test 3: Num courses == 2, prereqs form cycle
n = 2
prereqs = [[0, 1], [1, 0]]
course_order = Solution().findOrder(n, prereqs)
expected = []
assert course_order == expected, f"Expected {expected} but got {course_order}"

# Test 4: Num courses == 2, prereqs no cycle
n = 2
prereqs = [[0, 1]]
course_order = Solution().findOrder(n, prereqs)
expected = [1, 0]
assert course_order == expected, f"Expected {expected} but got {course_order}"

# Test 5: Num courses > 2, some prereqs
n = 3
prereqs = [[1, 0], [2, 0], [2, 1]]
course_order = Solution().findOrder(n, prereqs)
expected = [0, 1, 2]
assert course_order == expected, f"Expected {expected} but got {course_order}"

# Test 6: Num courses > 2, some multiple prereqs
n = 3
prereqs = [[1, 0], [1, 3], [2, 0]]
course_order = Solution().findOrder(n, prereqs)
expected = [0, 3, 1, 2]
assert course_order == expected, f"Expected {expected} but got {course_order}"
