from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        stack = []

        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            result.append(root.val)
            root = root.right

        return result

"""
Explanation:

Iterate over tree using stack to keep track of nodes. Start by pushing all the left nodes into the stack and then adding the value to the result. Then move to the right node. Repeat until all nodes have been processed.

Notes:

Time complexity: O(n)
Space complexity: O(n), where n is the number of nodes in the binary tree
"""

# Test 1: Empty tree
inorder = Solution().inorderTraversal(None)
assert inorder == []

# Test 2: Tree w/ 1 node
t = TreeNode(1)
inorder = Solution().inorderTraversal(t)
assert inorder == [1]

# Test 3: Tree w/ multiple nodes
t = TreeNode(3)
t.left = TreeNode(2)
t.right = TreeNode(5)
t.left.left = TreeNode(1)
t.left.right = TreeNode(4)
t.right.right = TreeNode(6)
inorder = Solution().inorderTraversal(t)
assert inorder == [1, 2, 4, 3, 5, 6]