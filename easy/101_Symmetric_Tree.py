from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def dfs(n1, n2):
            if n1 == None and n2 == None:
                return True
            if n1 == None or n2 == None or n1.val != n2.val:
                return False

            return dfs(n1.left, n2.right) and dfs(n1.right, n2.left)

        return dfs(root, root)


"""
Explanation:

Return the call to helper function dfs with root node as n1 and n2, initiating the comparison of the entire tree. If both n1 and n2 are null, return true. If either n1 or n2 is null, or the values of n1 and n2 are not equal, return false. Otherwise, return the result of two recursive calls to dfs, one with n1.left and n2.right, and the other with n1.right and n2.left.

Notes:

Time complexity: O(n), where n is the number of nodes in the binary tree.

Space complexity: O(h), where h is the height of the binary tree.
"""

# Test 1: Single node in tree
t = TreeNode(1)
is_symmetric = Solution().isSymmetric(t)
assert is_symmetric == True, f"Expected True but got {is_symmetric}"

# Test 2: Symmetric tree
t = TreeNode(1)
t.left = TreeNode(2)
t.right = TreeNode(2)
t.left.left = TreeNode(3)
t.right.right = TreeNode(3)
t.left.right = TreeNode(4)
t.right.left = TreeNode(4)
is_symmetric = Solution().isSymmetric(t)
assert is_symmetric == True, f"Expected True but got {is_symmetric}"

# Test 3: Asymmetric tree
t = TreeNode(1)
t.left = TreeNode(1)
t.right = TreeNode(2)
t.left.left = TreeNode(3)
t.right.right = TreeNode(4)
t.left.right = TreeNode(5)
t.right.left = TreeNode(6)
is_symmetric = Solution().isSymmetric(t)
assert is_symmetric == False, f"Expected False but got {is_symmetric}"
