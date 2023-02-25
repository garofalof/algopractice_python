from typing import Optional


class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        curr = root
        successor = None

        while curr:
            if p.val >= curr.val:
                curr = curr.right
            else:
                successor = curr
                curr = curr.left

        return successor


"""
Explanation:

Initialize the current node to be the root node and the potential successor node to be None. Then, while the current node is not None, check whether the value of p >= value of curr. If it is, the inorder successor of p must be in the right subtree of curr, so update curr to be its right child. If p < value of curr, the inorder successor of p could be in the left subtree or could be curr itself, so update successor to be curr and then updates curr to be its left child. At the end of the loop, successor will hold the node that is the inorder successor of p, or None if there is no such node, so we return successor.

Notes:

Time complexity: O(n), as a skewed tree would have us searching each node of the BST in the worst case.

Space complexity: O(1) to store the current and successor node pointers.
"""

# Test 1: Single node
tree = TreeNode(1)
target = tree
successor = Solution().inorderSuccessor(tree, target)
expected = None
assert successor == expected, f"Expected {expected} but got {successor}"

# Test 2: Target node has right child
tree = TreeNode(2, TreeNode(1, None, TreeNode(4)))
target = tree.left
successor = Solution().inorderSuccessor(tree, target)
expected = tree.left.right
assert successor == expected, f"Expected {expected} but got {successor}"

# Test 3: Target node has no child
tree = TreeNode(3, TreeNode(2))
target = tree.left
successor = Solution().inorderSuccessor(tree, target)
expected = tree
assert successor == expected, f"Expected {expected} but got {successor}"

# Test 4: Target is largest in tree
tree = TreeNode(3, TreeNode(2), TreeNode(5, TreeNode(4), TreeNode(7)))
target = tree.right.right
successor = Solution().inorderSuccessor(tree, target)
expected = None
assert successor == expected, f"Expected {expected} but got {successor}"

# Test 5: Target is smallest in tree
tree = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)),
                TreeNode(6, TreeNode(5), TreeNode(7)))
target = tree.left.left
successor = Solution().inorderSuccessor(tree, target)
expected = tree.left
assert successor == expected, f"Expected {expected} but got {successor}"
