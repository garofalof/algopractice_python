class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        stack = [[root, root.val]]
        count = 0

        while stack:
            curr, max_val = stack.pop()

            if curr:
                if curr.val >= max_val:
                    count += 1

                new_max = max(max_val, curr.val)
                stack.append([curr.left, new_max])
                stack.append([curr.right, new_max])

        return count


"""
Explanation:

Initialize a stack with the root node and its value as a list. Also initialize a count variable to 0. Then enter into a loop that runs while the stack has work. In each iteration of the loop, pop the top element from the stack, which is a list consisting of a node and its max ancestor value along the path from the root node. If the node is not None, check if the node's value >= the max ancestor value. If it is, increment the count variable.

Next, calculate the new max ancestor value, which is the max of the current max ancestor value and the node's value. Then push the node's left and right child nodes and their corresponding new max ancestor values onto the stack as lists.

After the loop ends, return the count variable, which represents the number of good nodes in the binary tree.

Notes:

Time complexity: O(n), as we visit each node in the tree exactly once.

Space complexity: O(n), as we will keep max n / 2 nodes in the stack in the worst case when every right child has 2 children and every left child has no children.
"""

# Test 1: Single node
tree = TreeNode(1)
count = Solution().goodNodes(tree)
expected = 1
assert count == expected, f"Expected {expected} but got {count}"

# Test 2: Two nodes, second node smaller
tree = TreeNode(3, TreeNode(1))
count = Solution().goodNodes(tree)
expected = 1
assert count == expected, f"Expected {expected} but got {count}"

# Test 3: Two nodes, second node larger
tree = TreeNode(1, None, TreeNode(5))
count = Solution().goodNodes(tree)
expected = 2
assert count == expected, f"Expected {expected} but got {count}"

# Test 4: Three nodes, one smaller, one larger
tree = TreeNode(3, TreeNode(1), TreeNode(5))
count = Solution().goodNodes(tree)
expected = 2
assert count == expected, f"Expected {expected} but got {count}"

# Test 5: All larger in right subtree
tree = TreeNode(3, None, TreeNode(5, None, TreeNode(7, None, TreeNode(13))))
count = Solution().goodNodes(tree)
expected = 4
assert count == expected, f"Expected {expected} but got {count}"

# Test 6: All larger in left subtree
tree = TreeNode(3, TreeNode(5, TreeNode(
    7, TreeNode(9, TreeNode(13)), None)), None)
count = Solution().goodNodes(tree)
expected = 5
assert count == expected, f"Expected {expected} but got {count}"
