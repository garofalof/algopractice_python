from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        curr = slow
        prev = None

        while curr:
            curr.next, prev, curr = prev, curr, curr.next

        l1, l2 = head, prev

        while l2.next:
            l1.next, l1 = l2, l1.next
            l2.next, l2 = l1, l2.next


"""
Explanation:

First find the midpoint of the linked list. Then reverse the second half. Finally, interweave the two halves of the linked list. This will reorder the list such that the first element is followed by the last element, the second element is followed by the second to last element, and so on.

Notes:

Time complexity: O(n)

Space complexity: O(1), as we use a constant amount of extra space for the slow, fast, curr, and prev pointers.
"""

# Test 1: Single node
head = ListNode(1)
Solution().reorderList(head)
assert head.val == 1, f"Expected 1 but got {head.val}"

# Test 2: Two nodes
head = ListNode(1, ListNode(2))
Solution().reorderList(head)
assert head.val == 1, f"Expected 1 but got {head.val}"
assert head.next.val == 2, f"Expected 2 but got {head.next.val}"

# Test 3: Odd number of nodes
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
Solution().reorderList(head)
assert head.val == 1, f"Expected 1 but got {head.val}"
assert head.next.val == 5, f"Expected 5 but got {head.next.val}"
assert head.next.next.val == 2, f"Expected 2 but got {head.next.next.val}"
assert head.next.next.next.val == 4, f"Expected 4 but got {head.next.next.next.val}"
assert head.next.next.next.next.val == 3, f"Expected 3 but got {head.next.next.next.next.val}"

# Test 4: Even number of nodes
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
Solution().reorderList(head)
assert head.val == 1, f"Expected 1 but got {head.val}"
assert head.next.val == 4, f"Expected 4 but got {head.next.val}"
assert head.next.next.val == 2, f"Expected 2 but got {head.next.next.val}"
assert head.next.next.next.val == 3, f"Expected 2 but got {head.next.next.next.val}"
