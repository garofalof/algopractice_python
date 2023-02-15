from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        slow = fast = head

        while fast and n:
            fast = fast.next
            n -= 1

        if not fast:
            return head.next

        while fast.next:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

        return head


"""
Explanation:

Use 2 pointers, slow and fast, initialized to the head of the linked list. The fast pointer moves n steps ahead of the slow pointer. If the fast pointer reaches the end of the linked list before n steps, the head of the linked list is returned after removing the first node. Else, slow and fast move one step at a time until fast reaches the end of the linked list. At this point, slow will be pointing to the node before the node to be removed. Remove the nth node from the end by setting the next pointer of the node pointed by slow to the node after the one to be removed. Finally, return the head of the modified linked list.

Notes:

Time complexity: The solution involves a single pass through the linked list, so the time complexity is O(n), where n is the length of the linked list.

Space complexity: The solution uses only two pointers, so the space complexity is O(1).
"""

# Test 1: Single node
head = ListNode(1)
n = 1
removed = Solution().removeNthFromEnd(head, n)
expected = None
assert removed == expected, f"Expected {expected} but got {removed}"

# Test 2: Two nodes, remove end
head = ListNode(1, ListNode(2))
n = 1
removed = Solution().removeNthFromEnd(head, n)
assert removed.val == 1, f"Expected 1 but got {removed.val}"
assert removed.next == None, f"Expected None but got {removed.next}"

# Test 3: Two nodes, remove beginning
head = ListNode(1, ListNode(2))
n = 2
removed = Solution().removeNthFromEnd(head, n)
assert removed.val == 2, f"Expected 1 but got {removed.val}"
assert removed.next == None, f"Expected None but got {removed.next}"

# Test 4: Greater than two nodes, remove middle
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
n = 3
removed = Solution().removeNthFromEnd(head, n)
assert removed.val == 1, f"Expected 1 but got {removed.val}"
assert removed.next.val == 2, f"Expected 2 but got {removed.next.val}"
assert removed.next.next.val == 4, f"Expected 4 but got {removed.next.next.val}"
assert removed.next.next.next.val == 5, f"Expected 5 but got {removed.next.next.next.val}"
assert removed.next.next.next.next == None, f"Expected None but got {removed.next.next.next}"
