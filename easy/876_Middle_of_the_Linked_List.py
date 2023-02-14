from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head

        while fast and fast.next:
            slow, fast = slow.next, fast.next.next

        return slow


"""
Explanation:

Initialize a slow and fast pointer to point to the head node. The slow pointer moves one step at a time while the fast pointer moves two steps at a time. The fast pointer will reach the end of the linked list before the slow pointer reaches the middle node. Therefore, when the fast pointer reaches the end of the linked list, the slow pointer will be pointing to the middle node.

Notes:

Time complexity: O(n)

Space complexity: O(1)
"""

# Test 1: Single node
node = ListNode(1)
expected = node
middle = Solution().middleNode(node)
assert middle == expected, f"Expected {expected} but got {middle}"

# Test 2: Odd number of nodes
node = ListNode(1)
node.next = ListNode(2)
node.next.next = ListNode(3)
node.next.next.next = ListNode(4)
node.next.next.next.next = ListNode(5)
expected = node.next.next
middle = Solution().middleNode(node)
assert middle == expected, f"Expected {expected} but got {middle}"

# Test 3: Even number of nodes
node = ListNode(1)
node.next = ListNode(2)
node.next.next = ListNode(3)
node.next.next.next = ListNode(4)
expected = node.next.next
middle = Solution().middleNode(node)
assert middle == expected, f"Expected {expected} but got {middle}"
