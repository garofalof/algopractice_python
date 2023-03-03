from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        odd_head, even_head = head, head.next
        odd_tail, even_tail = odd_head, even_head

        while even_tail and even_tail.next:
            odd_tail.next = even_tail.next
            odd_tail = odd_tail.next
            even_tail.next = odd_tail.next
            even_tail = even_tail.next

        odd_tail.next = even_head

        return odd_head


"""
Explanation:

Check if the head of the linked list exists. If not, return None. Initialize two pointers, odd and even, to the head and the next node of the head respectively. Create a variable evenHead to store the head of the even list.

Loop through the linked list while even and even.next are not None.
- Set the next node of odd to be even.next
- Move odd to its next node
- Set the next node of even to be odd.next
- Move even to its next node

Once the loop is finished, set the next node of odd to be evenHead, which connects the end of the odd list to the start of the even list.

Return the head of the updated linked list.

Notes:

Time complexity: O(n), where n is the number of nodes in the linked list. We loop through the linked list once.

Space complexity: O(1), as we use constant extra space to store the pointers.
"""

# Test 1: Empty list
root = None
odd_even_list = Solution().oddEvenList(root)
expected = None
assert odd_even_list == expected, f"Expected {expected} but got {odd_even_list}"

# Test 2: Single node
root = ListNode(1)
odd_even_list = Solution().oddEvenList(root)
expected = 1
assert odd_even_list.val == expected, f"Expected {expected} but got {odd_even_list.val}"

# Test 3: Two nodes
root = ListNode(1, ListNode(2))
odd_even_list = Solution().oddEvenList(root)
expected = 1
assert odd_even_list.val == expected, f"Expected {expected} but got {odd_even_list.val}"
expected = 2
assert odd_even_list.next.val == expected, f"Expected {expected} but got {odd_even_list.next.val}"

# Test 4: Odd number of nodes
root = ListNode(1, ListNode(2, ListNode(3)))
odd_even_list = Solution().oddEvenList(root)
expected = 1
assert odd_even_list.val == expected, f"Expected {expected} but got {odd_even_list.val}"
expected = 3
assert odd_even_list.next.val == expected, f"Expected {expected} but got {odd_even_list.next.val}"
expected = 2
assert odd_even_list.next.next.val == expected, f"Expected {expected} but got {odd_even_list.next.next.val}"

# # Test 5: Even number of nodes
root = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
odd_even_list = Solution().oddEvenList(root)
expected = 1
assert odd_even_list.val == expected, f"Expected {expected} but got {odd_even_list.val}"
expected = 3
assert odd_even_list.next.val == expected, f"Expected {expected} but got {odd_even_list.next.val}"
expected = 2
assert odd_even_list.next.next.val == expected, f"Expected {expected} but got {odd_even_list.next.next.val}"
expected = 4
assert odd_even_list.next.next.next.val == expected, f"Expected {expected} but got {odd_even_list.next.next.next.val}"
