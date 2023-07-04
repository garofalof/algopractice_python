from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        node_map = {}

        def build_node_map(node, parent):
            if node:
                node_map[node] = parent
                build_node_map(node.left, node)
                build_node_map(node.right, node)

        build_node_map(root, None)

        result = []
        visited = set()

        def dfs(node, k):
            if not node or node in visited:
                return
            if k == 0:
                result.append(node.val)
                return

            visited.add(node)

            dfs(node.left, k - 1)
            dfs(node.right, k - 1)
            dfs(node_map.get(node), k - 1)

        dfs(target, k)

        return result


"""
Explanation:

Create a `node_map` dictionary, which maps each node to its parent. This mapping is created by traversing the binary tree using a recursive helper function called `build_node_map`. Next, initialize an empty list `result` to store the node values at distance k and create a `visited` set to keep track of visited nodes during the traversal.

The main traversal happens in the DFS function. It takes a node and the current k distance as input. It first checks if the node is either null or has been visited before. If so, it returns to exit. If k becomes zero, it means we have reached a node at the desired distance from the target. In this case, we append the node's value to the result list and return to exit. If the above conditions are not met, we add the current node to the visited set to mark it as visited. Then we recursively call dfs on the left child, right child, and the parent of the current node. The k distance is reduced by 1 in each recursive call.

After the DFS function completes, the result list contains the node values at distance k from the target node and is returned as output.

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
