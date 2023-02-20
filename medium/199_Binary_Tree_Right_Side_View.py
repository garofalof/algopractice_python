from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        q = deque()
        q.append(root)

        if not root:
            return result

        while q:
            size = len(q)

            for i in range(size):
                curr = q.popleft()

                if i == size - 1:
                    result.append(curr.val)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)

        return result


"""
Explanation:

Create an empty list to store the result and a queue. Add the root node to the queue. If the root is None, return an empty list. While queue is not empty, we find the size of the queue and iterate through each element in the queue. For each element, pop it from the front of the queue and check if it's the last element in the current level. If it's the last element, add its value to the result list. Next, add the left and right children of the current node to the queue if they exist. Once done, return the result list.

Notes:

Time complexity: O(n), where n is the number of nodes in the tree, as we visit each node once.

Space complexity: O(n), since in the worst case, the queue will store all the nodes in the last level of the tree.
"""

# Test 1: Empty root
root = None
right_side = Solution().rightSideView(root)
expected = []
assert right_side == expected, f"Expected {expected} but got {right_side}"

# Test 2: Single node tree
root = TreeNode(1)
right_side = Solution().rightSideView(root)
expected = [1]
assert right_side == expected, f"Expected {expected} but got {right_side}"

# Test 3: Tree with multiple nodes and all nodes have right child
root = TreeNode(1, None, TreeNode(2, None, TreeNode(3)))
right_side = Solution().rightSideView(root)
expected = [1, 2, 3]
assert right_side == expected, f"Expected {expected} but got {right_side}"

# Test 4: Tree with multiple nodes and all nodes have left child
root = TreeNode(1, TreeNode(2, TreeNode(3)), TreeNode(4, TreeNode(5)))
right_side = Solution().rightSideView(root)
expected = [1, 4, 5]
assert right_side == expected, f"Expected {expected} but got {right_side}"

# Test 5: Tree with multiple nodes and varying number of left and right children
root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)),
                TreeNode(3, None, TreeNode(6)))
right_side = Solution().rightSideView(root)
expected = [1, 3, 6]
assert right_side == expected, f"Expected {expected} but got {right_side}"
