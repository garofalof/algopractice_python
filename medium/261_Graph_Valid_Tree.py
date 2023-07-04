from typing import List


class Solution:
    def valid_tree(self, n: int, edges: List[List[int]]) -> bool:
        graph = {i: [] for i in range(n)}
        visited = set()

        for node, edge in edges:
            graph[node].append(edge)
            graph[edge].append(node)

        def dfs(node, prev):
            if node in visited:
                return False

            visited.add(node)

            for edge in graph.get(node):
                if edge == prev:
                    continue
                if not dfs(edge, node):
                    return False

            return True

        return dfs(0, -1) and n == len(visited)


"""
Explanation:

Initialize an empty dictionary `graph` and a set `visited`. Next, build the graph by iterating through the list of edges. For each edge, add the corresponding nodes to each other's adjacency list in the graph. After setting up the graph, perform a DFS on the graph starting from the first node, marking visited nodes in the visited set. The dfs function recursively calls itself on each unvisited neighbor of the current node, except for the previous node to avoid revisiting it.

Finally, we return true for a valid tree if: 1) the DFS traversal covers all the nodes in the graph, which is determined by comparing the length of the visited set with the total number of nodes; and 2) whether there are no cycles or disconnected components in the graph, which is ensured by the DFS function's return value.

Notes:

Time complexity: O(nodes + edges)

Space complexity: O(nodes)
"""

# Test Case 1: Basic test case with a valid tree
n = 5
edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
result = Solution().valid_tree(n, edges)
expected = True
assert result == expected, f"Expected {expected} but got {result}"

# Test Case 2: Basic test case with an invalid tree (cycle)
n = 4
edges = [[0, 1], [1, 2], [2, 3], [3, 0]]
result = Solution().valid_tree(n, edges)
expected = False
assert result == expected, f"Expected {expected} but got {result}"

# Test Case 3: Basic test case with an invalid tree (disconnected component)
n = 4
edges = [[0, 1], [2, 3]]
result = Solution().valid_tree(n, edges)
expected = False
assert result == expected, f"Expected {expected} but got {result}"

# Test Case 4: Test case with single node, which is considered a valid tree
n = 1
edges = []
result = Solution().valid_tree(n, edges)
expected = True
assert result == expected, f"Expected {expected} but got {result}"

# Test Case 5: Test case with multiple nodes and no edges, which is considered an invalid tree
n = 3
edges = []
result = Solution().valid_tree(n, edges)
expected = False
assert result == expected, f"Expected {expected} but got {result}"
