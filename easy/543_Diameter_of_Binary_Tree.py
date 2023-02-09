from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.diameter = 0

        def dfs(node):
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)
            self.diameter = max(self.diameter, left + right)

            return 1 + max(left, right)

        dfs(root)

        return self.diameter


"""
Explanation:

Create a dfs function to traverse the binary tree and calculate the diameter. Initialize a variable diameter to 0. In the dfs function, if the node is None, return 0. Calculate the diameter of the left and right subtrees using the dfs function recursively. Update the diameter variable with the maximum value of left + right or the current diameter. Return the maximum diameter of the left or right subtree plus 1 to account for the parent node. The final diameter is the diameter of the binary tree.

Notes:

Time complexity: O(n)
Space complexity: O(n)
"""

# Test 1: Single node tree
t1 = TreeNode(val=1)
diameter = Solution().diameterOfBinaryTree(t1)
assert diameter == 0, f"Expected 0 but got {diameter}"

# Test 2: Complete binary tree
t2 = TreeNode(val=1)
t2.left = TreeNode(val=2)
t2.right = TreeNode(val=3)
t2.left.left = TreeNode(val=4)
t2.left.right = TreeNode(val=5)
t2.right.left = TreeNode(val=6)
t2.right.right = TreeNode(val=7)
diameter = Solution().diameterOfBinaryTree(t2)
assert diameter == 4, f"Expected 4 but got {diameter}"

# Test 3: Unbalanced tree
t3 = TreeNode(val=1)
t3.left = TreeNode(val=2)
t3.left.left = TreeNode(val=3)
t3.left.left.left = TreeNode(val=4)
diameter = Solution().diameterOfBinaryTree(t3)
assert diameter == 3, f"Expected 3 but got {diameter}"

# Test 4: Tree with negative values
t4 = TreeNode(val=-1)
t4.left = TreeNode(val=-2)
t4.right = TreeNode(val=-3)
t4.left.left = TreeNode(val=-4)
t4.right.right = TreeNode(val=-5)
diameter = Solution().diameterOfBinaryTree(t4)
assert diameter == 4, f"Expected 3 but got {diameter}"
