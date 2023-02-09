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

# Explanation:
# -Initialize stack and result as empty arrays
# -While curr node not null or stack has work:
# -While curr node not null, push curr to stack and set curr to left child
# -Once we go all the way left, pop last node off stack and push node val to result
# -Then set curr to right child and continue
# -Once done, return result

# Notes:
# -Time complexity: O(n)
# -Space complexity: O(n)

t = TreeNode(3)
t.left = TreeNode(2)
t.right = TreeNode(5)
t.left.left = TreeNode(1)
t.left.right = TreeNode(4)
t.right.right = TreeNode(6)
inorder = Solution().inorderTraversal(t)

print(f"Inorder traversal is {inorder}")