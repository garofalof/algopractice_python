from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack = [root]

        while stack:
            curr = stack.pop()

            if curr:
                curr.left, curr.right = curr.right, curr.left
                stack.append(curr.left)
                stack.append(curr.right)

        return root

"""
Explanation:

Initialize a stack w/ the root node. While the stack has work, pop the current node `curr` from the stack. If curr is not null, swap the left and right child nodes of curr. Then, append the left and right child nodes of curr to the stack if they exist.

By swapping the left and right child nodes at each node, the function inverts the binary tree. This process continues until all nodes have been processed.

Finally, return the root of the inverted binary tree once done processing.

Notes:

Time complexity: O(n), where n is the number of nodes in the binary tree, as each node is processed once.
Space complexity: O(n), as the stack size can grow up to the number of nodes in the binary tree in the worst case.
"""

def is_same_tree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    if not p and not q:
        return True
    if not p or not q:
        return False
    if p.val != q.val:
        return False
    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)

# Test Case 1: Empty tree
root = None
result = Solution().invertTree(root)
expected = None
assert is_same_tree(result, expected), f"Expected {expected} but got {result}"

# Test Case 2: Single node
root = TreeNode(1)
result = Solution().invertTree(root)
expected = TreeNode(1)
assert is_same_tree(result, expected), f"Expected {expected} but got {result}"

# Test Case 3: Balanced tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
result = Solution().invertTree(root)
expected = TreeNode(1)
expected.left = TreeNode(3)
expected.right = TreeNode(2)
expected.left.left = TreeNode(7)
expected.left.right = TreeNode(6)
expected.right.left = TreeNode(5)
expected.right.right = TreeNode(4)
assert is_same_tree(result, expected), f"Expected {expected} but got {result}"

# Test Case 4: Skewed tree
root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
result = Solution().invertTree(root)
expected = TreeNode(1)
expected.right = TreeNode(2)
expected.right.left = TreeNode(5)
expected.right.right = TreeNode(4)