from typing import Optional

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution:
    def __init__(self):
        self.diameter = 0

    def dfs(self, node: Optional[TreeNode]) -> int:
        if not node:
            return 0

        left = self.dfs(node.left)
        right = self.dfs(node.right)

        self.diameter = max(self.diameter, left + right)

        return 1 + max(left, right)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.dfs(root)

        return self.diameter

t = TreeNode(3)
t.left = TreeNode(2)
t.right = TreeNode(4)
t.left.left = TreeNode(1)
t.right.right = TreeNode(5)
diameter = Solution().diameterOfBinaryTree(t)

print(f"Diameter of binary tree is {diameter}")

# Explanation:
# -Set diameter to 0
# -For each node starting from root:
# -If node is null, return 0
# -Set left and right to result of dfs on left/right subtrees
# -Update diameter to max of diameter or left + right distance
# -Return max of left or right subtree diameter + 1 to account for parent

# Notes:
# -Time complexity: O(n), as we only enter/exit from each node once
# -Space complexity: O(n)