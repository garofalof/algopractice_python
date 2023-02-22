class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while root:
            if root.val < p.val and root.val < q.val:
                root = root.right
            elif root.val > p.val and root.val > q.val:
                root = root.left
            else:
                break

        return root


"""
Explanation:

Use a single while loop to traverse the binary search tree to find the lowest common ancestor of nodes p and q. Start by checking if the current root value is less than both p and q values, and if it is, move to the right subtree. If the current root value is greater than both p and q values, move to the left subtree. Otherwise, we have found the lowest common ancestor and we return the current root.

Notes:

Time complexity: O(n), as the worst case, where the tree can be skewed, leads to O(n) time complexity, where n is the number of nodes in the tree.

Space complexity: O(1), as we only use a fixed number of pointers to traverse the tree.
"""

# Test case 1: Both p and q are in the left subtree
root = TreeNode(6)
root.left = TreeNode(2)
root.right = TreeNode(8)
root.left.left = TreeNode(0)
root.left.right = TreeNode(4)
root.left.right.left = TreeNode(3)
root.left.right.right = TreeNode(5)

p = root.left
q = root.left.right
common_ancestor = Solution().lowestCommonAncestor(root, p, q)
expected = root.left
assert common_ancestor == expected, f"Expected {expected} but got {common_ancestor}"

# Test case 2: Both p and q are in the right subtree
root = TreeNode(6)
root.left = TreeNode(2)
root.right = TreeNode(8)
root.right.left = TreeNode(7)
root.right.right = TreeNode(9)

p = root.right.left
q = root.right.right
common_ancestor = Solution().lowestCommonAncestor(root, p, q)
expected = root.right
assert common_ancestor == expected, f"Expected {expected} but got {common_ancestor}"

# Test case 3: p is the root
root = TreeNode(6)
root.left = TreeNode(2)
root.right = TreeNode(8)
root.left.left = TreeNode(0)
root.left.right = TreeNode(4)
root.left.right.left = TreeNode(3)
root.left.right.right = TreeNode(5)

p = root
q = root.left.right
common_ancestor = Solution().lowestCommonAncestor(root, p, q)
expected = root
assert common_ancestor == expected, f"Expected {expected} but got {common_ancestor}"

# Test case 4: q is the root
root = TreeNode(6)
root.left = TreeNode(2)
root.right = TreeNode(8)
root.right.left = TreeNode(7)
root.right.right = TreeNode(9)

p = root.left
q = root
common_ancestor = Solution().lowestCommonAncestor(root, p, q)
expected = root
assert common_ancestor == expected, f"Expected {expected} but got {common_ancestor}"

# Test case 5: p and q are in different subtrees
root = TreeNode(6)
root.left = TreeNode(2)
root.right = TreeNode(8)
root.left.left = TreeNode(0)
root.left.right = TreeNode(4)
root.left.right.left = TreeNode(3)
root.left.right.right = TreeNode(5)

p = root.left.right.left
q = root.right
common_ancestor = Solution().lowestCommonAncestor(root, p, q)
expected = root
assert common_ancestor == expected, f"Expected {expected} but got {common_ancestor}"

# Test case 6: Both p and q are at the same level but not in the same subtree
root = TreeNode(6)
root.left = TreeNode(2)
root.right = TreeNode(8)
root.left.left = TreeNode(0)
root.left.right = TreeNode(4)
root.left.right.left = TreeNode(3)
root.left.right.right = TreeNode(5)
root.right.left = TreeNode(7)
root.right.right = TreeNode(9)

p = root.left.left
q = root.right.right
common_ancestor = Solution().lowestCommonAncestor(root, p, q)
expected = root
assert common_ancestor == expected, f"Expected {expected} but got {common_ancestor}"

# Test case 7: p and q are the only two nodes in the tree
root = TreeNode(6)
root.left = TreeNode(1)
p = root
q = root.left
common_ancestor = Solution().lowestCommonAncestor(root, p, q)
expected = root
assert common_ancestor == expected, f"Expected {expected} but got {common_ancestor}"