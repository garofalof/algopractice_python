from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        stack = [(root, 0, None)]
        node_map = {}
        p_depth, q_depth = 0, 0

        while stack:
            node, depth, parent = stack.pop()

            if node:
                node_map[node] = parent
                p_depth = depth if node == p else p_depth
                q_depth = depth if node == q else q_depth

                stack.append((node.left, depth + 1, node))
                stack.append((node.right, depth + 1, node))

        steps = abs(p_depth - q_depth)
        lowest = p if p_depth > q_depth else q
        highest = p if p.val != lowest.val else q

        for _ in range(steps):
            lowest = node_map.get(lowest)

        while lowest != highest:
            lowest, highest = node_map.get(lowest), node_map.get(highest)

        return lowest

"""
Explanation:

Initialize a stack w/ the root node and its depth as 0. Additionally, initialize a dictionary `node_map` to store the parent nodes of each visited node. Keep track of the depths of nodes p and q as `p_depth` and `q_depth`, respectively.

While the stack is not empty, pop a node from the stack along w/ its depth and parent node. Update the node_map w/ the parent node of the current node. Check if the current node is p or q and update their respective depths accordingly. Continue to traverse the left and right children of each node, incrementing the depth by 1 and updating the parent node in the stack.

After the traversal, calculate the number of steps needed to reach the lowest common ancestor by taking the absolute difference between the depths of p and q. Determine which node has the greater depth and assigns it to lowest, while the other node is assigned to highest. Next, iteratively move lowest upward by accessing its parent node in the node_map for the number of steps calculated. This ensures that both lowest and highest are at the same depth. Finally, traverse upwards from lowest and highest in parallel using the node_map until they meet at the lowest common ancestor. Once a match is found, return the lowest common ancestor node.

Notes:

Time complexity: O(n), where n is the number of nodes in the binary tree

Space complexity: O(n), as the algorithm utilizes additional space for the stack and node_map
"""

# Test Case 1: p and q same level, different branches
tree = TreeNode(1, TreeNode(3), TreeNode(5))
p = tree.left
q = tree.right
result = Solution().lowestCommonAncestor(tree, p, q)
expected = tree
assert result == expected, f"Expected {expected} but got {result}"

# Test Case 2: Min number of nodes
tree = TreeNode(1, TreeNode(3), None)
p = tree
q = tree.left
result = Solution().lowestCommonAncestor(tree, p, q)
expected = tree
assert result == expected, f"Expected {expected} but got {result}"

# Test Case 3: p ancestor of q
tree = TreeNode(1, TreeNode(3, TreeNode(4, None, TreeNode(8)), TreeNode(7)), None)
p = tree.left
q = tree.left.left.right
result = Solution().lowestCommonAncestor(tree, p, q)
expected = tree.left
assert result == expected, f"Expected {expected} but got {result}"

# Test Case 4: q ancestor of p
tree = TreeNode(1, TreeNode(3, TreeNode(4, None, TreeNode(8)), TreeNode(7)), None)
p = tree.left.left.right
q = tree.left
result = Solution().lowestCommonAncestor(tree, p, q)
expected = tree.left
assert result == expected, f"Expected {expected} but got {result}"

# Test Case 5: p and q different levels, different branches
tree = TreeNode(1, TreeNode(3, TreeNode(4), TreeNode(7, TreeNode(9), TreeNode(12))), TreeNode(5, TreeNode(6), TreeNode(10)))
p = tree.left.right.left
q = tree.right
result = Solution().lowestCommonAncestor(tree, p, q)
expected = tree
assert result == expected, f"Expected {expected} but got {result}"