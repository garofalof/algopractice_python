from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack = [[root, 1]]
        maxDepth = 0

        while stack:
            curr, depth = stack.pop()

            if curr:
                maxDepth = max(depth, maxDepth)
                stack.append([curr.left, depth + 1])
                stack.append([curr.right, depth + 1])

        return maxDepth

"""
Explanation:

Initialize a stack with the root node and its depth set to 1. Set maxDepth to 0, which stores the maximum depth encountered. While the stack is not empty, pop a node from the stack. If the node is not null, update maxDepth with the max value between the current depth and maxDepth. Push the left and right children of the node onto the stack with their depths incremented by 1. Once done, return maxDepth as the maximum depth of the binary tree.

Notes:

Time complexity: O(n), where n is the number of nodes in the binary tree, because we need to visit each node exactly once.

Space complexity: O(h), where h is the max height of the binary tree. In the worst case, where the binary tree is skewed and has a height of n (all nodes form a single branch), the stack can hold up to n elements.
"""

# Test 1: Empty binary tree
root = None
max_depth = Solution().maxDepth(root)
expected = 0
assert max_depth == expected, f"Expected {expected} but got {max_depth}"

# Test 2: Single-node binary tree
root = TreeNode(1)
max_depth = Solution().maxDepth(root)
expected = 1
assert max_depth == expected, f"Expected {expected} but got {max_depth}"

# Test 3: Balanced binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
max_depth = Solution().maxDepth(root)
expected = 2
assert max_depth == expected, f"Expected {expected} but got {max_depth}"

# Test 4: Binary tree with balanced and skewed structure
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.right.right = TreeNode(5)
max_depth = Solution().maxDepth(root)
expected = 3
assert max_depth == expected, f"Expected {expected} but got {max_depth}"

# Test 5: Skewed binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(3)
root.left.left.left = TreeNode(4)
root.left.left.left.left = TreeNode(5)
max_depth = Solution().maxDepth(root)
expected = 5
assert max_depth == expected, f"Expected {expected} but got {max_depth}"