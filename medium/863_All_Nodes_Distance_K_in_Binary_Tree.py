class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.visited = set()
        self.parents = {}

    def distanceK(self, root, target, k):
        result = []

        def findTarget(node, parent, target):
            if not node:
                return None

            self.parents[node] = parent

            if node == target:
                return node

            return findTarget(node.left, node, target) or findTarget(node.right, node, target)

        def findKApart(node, k, result):
            if not node or node in self.visited:
                return

            if k == 0:
                result.append(node.val)
                return

            self.visited.add(node)

            findKApart(node.left, k - 1, result)
            findKApart(node.right, k - 1, result)

            if node in self.parents:
                findKApart(self.parents[node], k - 1, result)

        node = findTarget(root, None, target)

        findKApart(node, k, result)

        return result


"""
Explanation:

First, initialize an empty result list, a set of visited nodes, and a dictionary parents that maps each node to its parent. Then define a helper function findTarget that takes in a node, its parent, and the target node, and returns the target node if found, and otherwise recursively calls itself on the node's left and right children. While traversing the tree, populate the parents dictionary with each node and its parent.

Next, define another helper function findKApart that takes in a node, a distance k, and the result list. First check if the node is None or has been visited. If it hasn't, and k is 0, append the node's value to the result list. Otherwise, we mark the node as visited, and recursively call findKApart on the node's left and right children with k-1. We also check if the current node has a parent in the parents dictionary, and if so, recursively call findKApart on the parent with k-1.

Finally, call findTarget on the root node to find the target node. Then call findKApart on the target node with k and the result list. Once done, return the result list.

Notes:

Time Complexity: O(n), where n is the number of nodes in the binary tree. We traverse the entire tree twice, once to populate the parents dictionary, and once to find nodes at distance k from the target.

Space Complexity: O(n), where n is the number of nodes in the binary tree. We store the visited set, the parents dictionary, and the result list, each of which can contain up to n nodes.
"""

# Test 1: Single node, k == 0
root = TreeNode(1)
target = root
k = 0
k_nodes = Solution().distanceK(root, target, k)
expected = [1]
assert k_nodes == expected, f"Expected {expected} but got {k_nodes}"

# Test 2: Single node, k > 0
root = TreeNode(1)
target = root
k = 1
k_nodes = Solution().distanceK(root, target, k)
expected = []
assert k_nodes == expected, f"Expected {expected} but got {k_nodes}"

# Test 3: Target node is leaf
root = TreeNode(10, TreeNode(5), TreeNode(20, TreeNode(15)))
target = root.right.left
k = 1
k_nodes = Solution().distanceK(root, target, k)
expected = [20]
assert k_nodes == expected, f"Expected {expected} but got {k_nodes}"

# Test 4: Target node is child of root
root = TreeNode(10, TreeNode(5), TreeNode(20))
target = root.left
k = 1
k_nodes = Solution().distanceK(root, target, k)
expected = [10]
assert k_nodes == expected, f"Expected {expected} but got {k_nodes}"

# Test 5: Tree w/ multiple nodes and multiple k distance from target
root = TreeNode(10, TreeNode(5), TreeNode(20, TreeNode(15), TreeNode(25)))
target = root.right
k = 1
k_nodes = Solution().distanceK(root, target, k)
expected = [15, 25, 10]
assert k_nodes == expected, f"Expected {expected} but got {k_nodes}"

# Test 6: Tree w/ multiple nodes and no node k distance from target
root = TreeNode(10, TreeNode(5), TreeNode(20, TreeNode(15), TreeNode(25)))
target = root.right
k = 5
k_nodes = Solution().distanceK(root, target, k)
expected = []
assert k_nodes == expected, f"Expected {expected} but got {k_nodes}"
