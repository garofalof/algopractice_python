from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
            curr.next, prev, curr = prev, curr, curr.next

        return prev


"""
Explanation:

Initialize two pointers, prev and curr, to None and head respectively. These pointers are used to traverse through the linked list.

While curr pointer is not None, iterate through each node in the linked list until the end is reached. In each iteration, the current node's next pointer is set to the previous node. The prev pointer is then updated to the current node, and the curr pointer is set to the next node.

At the end of the loop, prev points to the new head node of the reversed linked list, which we return as the reversed list.

Notes:

Time complexity: O(n), where n is the number of nodes in the linked list

Space complexity: O(1), as the algorithm only uses a constant amount of additional memory to store the prev and curr pointers.
"""

# Test 1: Empty node
head = None
list_reversed = Solution().reverseList(head)
expected = None
assert list_reversed == expected, f"Expected {expected} but got {list_reversed}"

# Test 2: Single node
head = ListNode(1)
list_reversed = Solution().reverseList(head)
expected = head
assert list_reversed == expected, f"Expected {expected} but got {list_reversed}"

# Test 3: Even number of nodes
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
list_reversed = Solution().reverseList(head)
expected = 4
assert list_reversed.val == expected, f"Expected {expected} but got {list_reversed.val}"
expected = 3
assert list_reversed.next.val == expected, f"Expected {expected} but got {list_reversed.next.val}"
expected = 2
assert list_reversed.next.next.val == expected, f"Expected {expected} but got {list_reversed.next.next.val}"
expected = 1
assert list_reversed.next.next.next.val == expected, f"Expected {expected} but got {list_reversed.next.next.next.val}"

# Test 4: Odd number of nodes
head = ListNode(1, ListNode(2, ListNode(3)))
list_reversed = Solution().reverseList(head)
expected = 3
assert list_reversed.val == expected, f"Expected {expected} but got {list_reversed.val}"
expected = 2
assert list_reversed.next.val == expected, f"Expected {expected} but got {list_reversed.next.val}"
expected = 1
assert list_reversed.next.next.val == expected, f"Expected {expected} but got {list_reversed.next.next.val}"
