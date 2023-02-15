from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(n1, n2):
            if not n1 and not n2:
                return True
            if not n1 or not n2 or n1.val != n2.val:
                return False

            return dfs(n1.left, n2.left) and dfs(n1.right, n2.right)

        return dfs(p, q)


"""
Explanation:

Use a helper dfs function that takes in two nodes, n1 and n2, and compares them for equality. If both n1 and n2 are null, we've reached the end of the tree and the nodes match, so return True. If either n1 or n2 is null, or the values of n1 and n2 are not equal, the trees are not equal, so return False. Otherwise, make two recursive calls to dfs, one with n1.left and n2.left, and the other with n1.right and n2.right, to compare the subtrees. We then return the ANDed result of these two recursive calls.

Overall, the dfs function recursively compares the nodes of the two trees and returns True if all nodes match, and False otherwise.

Notes:

Time complexity: O(n), where n is the number of nodes in the binary tree, because we need to visit each node exactly once.

Space complexity: O(h), where h is the height of the binary tree.
"""

# Test 1: One tree empty
first = TreeNode(1)
second = None
are_same = Solution().isSameTree(first, second)
expected = False
assert are_same == expected, f"Expected {expected} but got {are_same}"

# Test 2: Both trees empty
first = None
second = None
are_same = Solution().isSameTree(first, second)
expected = True
assert are_same == expected, f"Expected {expected} but got {are_same}"

# Test 3: Both trees single node, same values
first = TreeNode(1)
second = TreeNode(1)
are_same = Solution().isSameTree(first, second)
expected = True
assert are_same == expected, f"Expected {expected} but got {are_same}"

# Test 4: Both trees single node, different values
first = TreeNode(1)
second = TreeNode(2)
are_same = Solution().isSameTree(first, second)
expected = False
assert are_same == expected, f"Expected {expected} but got {are_same}"

# Test 5: Both trees same structure, same values
first = TreeNode(1, TreeNode(2), TreeNode(3))
second = TreeNode(1, TreeNode(2), TreeNode(3))
are_same = Solution().isSameTree(first, second)
expected = True
assert are_same == expected, f"Expected {expected} but got {are_same}"

# Test 6: Both trees have same structure, different values
first = TreeNode(1, TreeNode(2), TreeNode(3))
second = TreeNode(1, TreeNode(3), TreeNode(2))
are_same = Solution().isSameTree(first, second)
expected = False
assert are_same == expected, f"Expected {expected} but got {are_same}"

# Test 7: Both trees have different structures
first = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
second = TreeNode(1, TreeNode(2), TreeNode(3))
are_same = Solution().isSameTree(first, second)
expected = False
assert are_same == expected, f"Expected {expected} but got {are_same}"
