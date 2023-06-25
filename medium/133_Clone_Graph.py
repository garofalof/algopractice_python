class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node', node_map={}) -> 'Node':
        if not node:
            return None

        if node in node_map:
            return node_map.get(node)

        clone = Node(node.val)
        node_map[node] = clone

        for edge in node.neighbors:
            clone.neighbors.append(self.cloneGraph(edge, node_map))

        return clone

"""
Explanation:

Check if the input node is null. If it is, return null, indicating an empty graph.

Next, if the given node already exists in the node map, return the corresponding clone node from the node_map. This is done to handle cases where the same node is encountered multiple times in the graph, ensuring that the clone of the node is reused instead of creating duplicates. If the given node is not null and is not present in the node map, create a new clone node with the same value as the original node. Then add the original node and its corresponding clone to the node map.

Next, iterate over each neighbor of the original node. For each neighbor, recursively call the cloneGraph function, passing the neighbor as the new node and the node map. This ensures that all the neighbors of the original node are cloned and connected correctly in the clone graph.

Finally, return the clone node, which represents a clone of the original graph with all its nodes and edges.

Notes:

Time complexity: O(n + e), where n is the number of nodes in the graph and e is the number of edges

Space complexity: O(n), where n is the number of nodes in the graph
"""

def is_same_graph(node1, node2):
    if not node1 and not node2:
        return True
    if not node1 or not node2:
        return False
    if node1.val != node2.val:
        return False

    visited = set()
    stack = [(node1, node2)]

    while stack:
        curr1, curr2 = stack.pop()

        if curr1 in visited:
            continue
        visited.add(curr1)

        if len(curr1.neighbors) != len(curr2.neighbors):
            return False

        stack.extend(zip(curr1.neighbors, curr2.neighbors))

    return True

# Test 1: Empty graph
node = None
clone = Solution().cloneGraph(node)
expected = None
assert is_same_graph(clone, expected), "Test case 1 failed"

# Test 2: Graph with a single node
node = Node(1)
clone = Solution().cloneGraph(node)
expected = Node(1)
assert is_same_graph(clone, expected), "Test case 2 failed"

# Test 3: Graph with two connected nodes
node1 = Node(1)
node2 = Node(2)
node1.neighbors = [node2]
node2.neighbors = [node1]
clone = Solution().cloneGraph(node1)
expected = Node(1)
expected_clone = Node(2)
expected.neighbors = [expected_clone]
expected_clone.neighbors = [expected]
assert is_same_graph(clone, expected), "Test case 3 failed"

# Test 4: Graph with multiple nodes and edges
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node1.neighbors = [node2, node3]
node2.neighbors = [node1, node3]
node3.neighbors = [node1, node2]
clone = Solution().cloneGraph(node1)
expected = Node(1)
expected_clone1 = Node(2)
expected_clone2 = Node(3)
expected.neighbors = [expected_clone1, expected_clone2]
expected_clone1.neighbors = [expected, expected_clone2]
expected_clone2.neighbors = [expected, expected_clone1]
assert is_same_graph(clone, expected), "Test case 4 failed"
