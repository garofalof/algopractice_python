import collections
from typing import Optional


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        q = collections.deque()
        q.append(root)

        while q:
            level_size = len(q)

            for i in range(level_size):
                curr = q.popleft()

                if curr:
                    if i < level_size - 1:
                        curr.next = q[0]
                    if curr.left:
                        q.append(curr.left)
                    if curr.right:
                        q.append(curr.right)

        return root


"""
Explanation:

Initialize a deque q and add the root node to it. Then enter a loop that runs as long as there are nodes in the queue.

Inside the loop, first determines the number of nodes in the current level of the tree by getting the length of the queue.

Then enter another loop that iterates over each node in the current level. At each iteration, remove the leftmost node from the queue and assign it to the variable curr.

If curr is not None, check if the current node is not the last node in the level. If it's not the last node, it sets the next pointer of curr to the leftmost node of the queue.

Then check if the current node has a left child and, if it does, add it to the queue. Similarly, check if the current node has a right child and, if it does, add it to the deque.

After the inner loop completes, returns the modified tree with next pointers set.

Notes:

Time complexity: O(n), as the algorithm traverses each node of the tree once.

Space complexity: O(n), as the queue can hold up to the maximum number of nodes in the last level of the tree. Therefore, the space complexity is O(n/2), or O(n), where n is the number of nodes in the tree.
"""

# Test 1: Empty tree
root = None
Solution().connect(root)
expected = None
assert root == expected, f"Expected {expected} but got {root}"

# Test 2: Single node
root = Node(1)
Solution().connect(root)
expected = None
assert root.next == expected, f"Expected {expected} but got {root.next}"

# Test 3: Balanced tree, 2 levels
root = Node(1, Node(2), Node(3))
Solution().connect(root)
expected = None
assert root.next == expected, f"Expected {expected} but got {root.next}"
expected = root.right
assert root.left.next == expected, f"Expected {expected} but got {root.left.next}"
expected = None
assert root.right.next == expected, f"Expected {expected} but got {root.right.next}"

# Test 4: Unbalanced tree, 2 levels
root = Node(1, Node(2))
Solution().connect(root)
expected = None
assert root.next == expected, f"Expected {expected} but got {root.next}"
expected = None
assert root.left.next == expected, f"Expected {expected} but got {root.left.next}"

# Test 5: All left children
root = Node(1, Node(2, Node(3, Node(4))))
Solution().connect(root)
expected = None
assert root.next == expected, f"Expected {expected} but got {root.next}"
assert root.left.next == expected, f"Expected {expected} but got {root.left.next}"
assert root.left.left.next == expected, f"Expected {expected} but got {root.left.left.next}"
assert root.left.left.left.next == expected, f"Expected {expected} but got {root.left.left.left.next}"

# Test 6: All right children
root = Node(1, None, Node(2, None, Node(3, None, Node(4))))
Solution().connect(root)
expected = None
assert root.next == expected, f"Expected {expected} but got {root.next}"
assert root.right.next == expected, f"Expected {expected} but got {root.right.next}"
assert root.right.right.next == expected, f"Expected {expected} but got {root.right.right.next}"
assert root.right.right.right.next == expected, f"Expected {expected} but got {root.right.right.right.next}"
