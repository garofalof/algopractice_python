from typing import List
from typing import Optional


class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        stack = [(root, 0)]
        level_map = {}

        while stack:
            curr, depth = stack.pop()

            if curr:
                if depth not in level_map:
                    level_map[depth] = []
                if depth % 2:
                    level_map[depth] = [curr.val] + level_map[depth]
                else:
                    level_map[depth].append(curr.val)

                stack.append((curr.right, depth + 1))
                stack.append((curr.left, depth + 1))

        return [val for _, val in level_map.items()]

"""
Explanation:

Initialize a stack stack w/ root node and depth of 0. Create a dictionary level_map to store the values of nodes at each level. While the stack is not empty, pop an node, depth tuple from the stack. Curr represents the current node, and depth represents the depth of that node.

If curr is not null, perform the following steps: iff the depth is not present as a key in level_map, create an empty list to store the values of nodes at that depth. If depth is an odd number, insert the value of the current node at the beginning of depth list to maintain the zigzag order. If depth is an even number, append the value of the current node to the depth list. Push the right child of curr and its depth onto the stack. Push the left child of curr and its depth onto the stack.

Finally, return the values from level_map as a list of lists once stack is empty.

Notes:

Time complexity: O(n ^ 2), as we concatenate the array inside the traversal at every other iteration, but can be brought down to O(n) using a queue.

Space complexity: O(n), where n is the number of nodes in the tree, as the space used in the stack and level_map is directly proportional to number of nodes in the tree.
"""

# Test Case 1: Empty tree
root = None
result = Solution().zigzagLevelOrder(root)
expected = []
assert result == expected, f"Expected {expected} but got {result}"

# Test Case 2: Single node
root = TreeNode(1)
result = Solution().zigzagLevelOrder(root)
expected = [[1]]
assert result == expected, f"Expected {expected} but got {result}"

# Test Case 3: Full binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
result = Solution().zigzagLevelOrder(root)
expected = [[1], [3, 2], [4, 5, 6, 7]]
assert result == expected, f"Expected {expected} but got {result}"

# Test Case 4: Skewed binary tree
root = TreeNode(1)
root.right = TreeNode(2)
root.right.right = TreeNode(3)
root.right.right.right = TreeNode(4)
root.right.right.right.right = TreeNode(5)
result = Solution().zigzagLevelOrder(root)
expected = [[1], [2], [3], [4], [5]]
assert result == expected, f"Expected {expected} but got {result}"

# Test Case 5: Binary tree with varying depths
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.right.right = TreeNode(5)
root.left.left.left = TreeNode(6)
result = Solution().zigzagLevelOrder(root)
expected = [[1], [3, 2], [4, 5], [6]]
assert result == expected, f"Expected {expected} but got {result}"

