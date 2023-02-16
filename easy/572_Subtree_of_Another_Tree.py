from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSame(n1, n2):
            if not n1 and not n2:
                return True
            if not n1 or not n2 or n1.val != n2.val:
                return False

            return isSame(n1.left, n2.left) and isSame(n1.right, n2.right)

        def dfs(n1, n2):
            if not n1:
                return False
            if n1.val == n2.val and isSame(n1, n2):
                return True

            return dfs(n1.left, n2) or dfs(n1.right, n2)

        return dfs(root, subRoot)

"""
Explanation:

Check if the subroot tree is a subtree of the root tree. Recursively traverse the larger tree and compare each node with the root of the smaller tree. If the nodes are equal, check if the two trees are the same using a separate helper function. If they are not the same, continue traversing the larger tree. If the traversal reaches the end of the larger tree and no match is found, return False. If a match is found, return True.

Notes:

Time complexity: O(n * m) in the worst case where the subRoot tree is a single path of nodes that extends from the root of the root tree.

Space complexity: O(m + n), where m and n are the number of nodes in the root and subRoot trees, respectively. This is because the space used by the two helper functions isSame() and dfs() are recursive in nature, and their maximum depth can be the height of the respective trees. Therefore, the space used by each recursive call of these functions can be proportional to the height of the trees. Since both root and subRoot trees are used in the recursion, the total space used can be proportional to the sum of the heights of these trees.
"""

# Test 1: Single node in both trees, not valid
root = TreeNode(1)
subroot = TreeNode(2)
is_subtree = Solution().isSubtree(root, subroot)
expected = False
assert is_subtree == expected, f"Expected {expected} but got {is_subtree}"

# Test 2: Single node in both trees, valid
root = TreeNode(1)
subroot = TreeNode(1)
is_subtree = Solution().isSubtree(root, subroot)
expected = True
assert is_subtree == expected, f"Expected {expected} but got {is_subtree}"

# Test 3: Single node subtree, not valid
root = TreeNode(1, TreeNode(2), TreeNode(3))
subroot = TreeNode(4)
is_subtree = Solution().isSubtree(root, subroot)
expected = False
assert is_subtree == expected, f"Expected {expected} but got {is_subtree}"

# Test 4: Single node subtree, valid
root = TreeNode(1, TreeNode(2), TreeNode(3))
subroot = TreeNode(2)
is_subtree = Solution().isSubtree(root, subroot)
expected = True
assert is_subtree == expected, f"Expected {expected} but got {is_subtree}"

# Test 5: Subtree in tree, not valid
root = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2, TreeNode(0))), TreeNode(5))
subroot = TreeNode(4, TreeNode(1), TreeNode(2))
is_subtree = Solution().isSubtree(root, subroot)
expected = False
assert is_subtree == expected, f"Expected {expected} but got {is_subtree}"

# Test 6: Subtree in tree, valid
root = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2)), TreeNode(5))
subroot = TreeNode(4, TreeNode(1), TreeNode(2))
is_subtree = Solution().isSubtree(root, subroot)
expected = True
assert is_subtree == expected, f"Expected {expected} but got {is_subtree}"

# Test 6: Subtree not in tree
root = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2)), TreeNode(5))
subroot = TreeNode(3, TreeNode(1), TreeNode(2))
is_subtree = Solution().isSubtree(root, subroot)
expected = False
assert is_subtree == expected, f"Expected {expected} but got {is_subtree}"