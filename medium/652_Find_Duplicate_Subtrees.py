from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        self.map = {}
        self.result = []

        self.dfs(root)

        return self.result

    def dfs(self, node):
        if not node:
            return "N"

        left = self.dfs(node.left)
        right = self.dfs(node.right)
        key = f"{node.val}-{left}-{right}"

        self.map[key] = self.map.get(key, 0) + 1

        if self.map[key] == 2:
            self.result.append(node)

        return key


"""
Explanation:

Initialize an empty dictionary map to keep track of the occurrence count of each subtree, and an empty list result to store the duplicate subtrees. Call the dfs function on the root node to traverse the tree and identify duplicate subtrees.

The dfs function performs a DFS traversal of the tree and constructs a unique key for each subtree encountered. If the current node is null, return the string "N" to represent a null node. Recursively call the dfs function on the left and right children of the current node to traverse the subtrees. Construct a key string by concatenating the value of the current node, the string representing the left subtree, and the string representing the right subtree. Increment the occurrence count of the key in the map dictionary. If the occurrence count becomes 2, add the current node to the result list as it represents a duplicate subtree. Return the key to pass it up to the parent node.

Once done, return the result list containing the duplicate subtrees.

Notes:

Time complexity: O(n), as we perform a DFS traversal, visiting each node in the tree only once

Space complexity: O(n), as the space used on recursion stack and in the map is directly proportional to the number of nodes in the tree
"""

# Test Case 1: Empty tree
root = None
result = Solution().findDuplicateSubtrees(root)
expected = []
assert result == expected, f"Expected {expected} but got {result}"

# Test Case 2: Single node tree
root = TreeNode(1)
result = Solution().findDuplicateSubtrees(root)
expected = []
assert result == expected, f"Expected {expected} but got {result}"

# Test Case 3: Tree with duplicate subtree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.right.left = TreeNode(3)
root.right.right = TreeNode(4)
result = Solution().findDuplicateSubtrees(root)
expected = [root.right.left]
assert result == expected, f"Expected {expected} but got {result}"

# Test Case 4: Tree with no duplicate subtree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
result = Solution().findDuplicateSubtrees(root)
expected = []
assert result == expected, f"Expected {expected} but got {result}"

# Test Case 5: Tree with duplicate subtrees at different levels
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.right.right = TreeNode(4)
root.left.left.left = TreeNode(5)
result = Solution().findDuplicateSubtrees(root)
expected = []
assert result == expected, f"Expected {expected} but got {result}"
