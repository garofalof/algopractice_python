from typing import Optional


class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        pointer_a = headA
        pointer_b = headB

        while pointer_a != pointer_b:
            pointer_a = pointer_a.next if pointer_a else headB
            pointer_b = pointer_b.next if pointer_b else headA

        return pointer_a

"""
Explanation:

Use 2 pointers, pointer_a and pointer_b, initialized to headA and headB, respectively. Traverse both linked lists simultaneously, moving the pointers 1 node at a time until both pointers meet at the intersection node of the two lists. If a pointer reaches the end of its list, the pointer is set to point to the head of the other list, allowing both pointers to travel the same distance before reaching the intersection node. If the pointers do not meet, return None indicating that there is no intersection.

Notes:

Time complexity: O(m + n), where m and n are the lengths of the input lists. This is because the two pointers traverse the lists simultaneously, traveling the same distance until they meet at the intersection node or reach the end of their respective lists.

Space complexity: O(1), as the function uses only two pointers to traverse the linked lists.
"""

# Test 1: Single pointers intersect
first_list = ListNode(1)
second_list = first_list
intersect_node = Solution().getIntersectionNode(first_list, second_list)
expected = first_list
assert intersect_node == expected, f"Expected {expected} but got {intersect_node}"

# Test 2: Single pointers don't intersect
first_list = ListNode(1)
second_list = ListNode(1)
intersect_node = Solution().getIntersectionNode(first_list, second_list)
expected = None
assert intersect_node == expected, f"Expected {expected} but got {intersect_node}"

# Test 3: One list single, one list multiple, no intersect
first_list = ListNode(1, ListNode(2, ListNode(3)))
second_list = ListNode(1)
intersect_node = Solution().getIntersectionNode(first_list, second_list)
expected = None
assert intersect_node == expected, f"Expected {expected} but got {intersect_node}"

# Test 4: One list single, one list multiple, intersect
first_list = ListNode(1, ListNode(2, ListNode(3)))
second_list = first_list.next
intersect_node = Solution().getIntersectionNode(first_list, second_list)
expected = first_list.next
assert intersect_node == expected, f"Expected {expected} but got {intersect_node}"

# Test 5: Both multiple, no intersect
first_list = ListNode(1, ListNode(2, ListNode(3)))
second_list = ListNode(4, ListNode(5, ListNode(6)))
intersect_node = Solution().getIntersectionNode(first_list, second_list)
expected = None
assert intersect_node == expected, f"Expected {expected} but got {intersect_node}"

# Test 6: Both multiple, intersect
first_list = ListNode(1, ListNode(2, ListNode(3, ListNode(7, ListNode(8)))))
second_list = ListNode(4, ListNode(5, first_list.next.next))
intersect_node = Solution().getIntersectionNode(first_list, second_list)
expected = first_list.next.next
assert intersect_node == expected, f"Expected {expected} but got {intersect_node}"