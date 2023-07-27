import heapq
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(min_heap, (node.val, i, node))

        dummy = ListNode()
        head = dummy

        while min_heap:
            _, list_idx, node = heapq.heappop(min_heap)
            head.next = node
            head = head.next

            if node.next:
                heapq.heappush(min_heap, (node.next.val, list_idx, node.next))

        return dummy.next


"""
Explanation:

Start by creating an empty min-heap and pushing the first node from each linked list into the heap. This ensures that the heap contains the smallest node from each list. Then, create a dummy node to act as the head of the merged list.

While the min-heap is not empty, pop the smallest node from the heap, append it to the merged list, and move the pointer to the next node in that linked list. If the next node exists, push it into the min-heap. Repeat this process until all nodes are processed.

Finally, return the next node of the dummy node, which is the head of the merged list.

Notes:

Time complexity: O(n log k), where k is the number of lists and n is the total number of nodes. At any time, the heap contains at most k nodes and there are n nodes to insert.

Space complexity: O(k), where k is the number of linkedlists.
"""


def compare_linked_lists(list1, list2):
    while list1 and list2:
        if list1.val != list2.val:
            return False
        list1 = list1.next
        list2 = list2.next

    return not list1 and not list2


# Test Case 1: Empty list
lists = []
result = Solution().mergeKLists(lists)
expected = None
assert result == expected, f"Expected {expected} but got {result}"

# Test Case 2: Only one linked list, and it is empty
lists = [None]
result = Solution().mergeKLists(lists)
expected = None
assert result == expected, f"Expected {expected} but got {result}"

# Test Case 3: Only one linked list, and it has one node
l1 = ListNode()
lists = [l1]
result = Solution().mergeKLists(lists)
expected = ListNode()
same_values = compare_linked_lists(result, expected)
assert same_values, f"Expected {expected} but got {result}"

# Test Case 4: Two linked lists with one node each
l1 = ListNode()
l2 = ListNode()
lists = [l1, l2]
result = Solution().mergeKLists(lists)
expected = ListNode(0, ListNode())
same_values = compare_linked_lists(result, expected)
assert same_values, f"Expected {expected} but got {result}"

# Test Case 5: Two linked lists with multiple nodes each
l1 = ListNode(1, ListNode(4, ListNode(5)))
l2 = ListNode(2, ListNode(3, ListNode(6)))
lists = [l1, l2]
result = Solution().mergeKLists(lists)
expected = ListNode(1, ListNode(2, ListNode(
    3, ListNode(4, ListNode(5, ListNode(6))))))
same_values = compare_linked_lists(result, expected)
assert same_values, f"Expected {expected} but got {result}"

# Test Case 6: Random test case with various lengths and values
l1 = ListNode(-1, ListNode(3, ListNode(4)))
l2 = ListNode(0, ListNode(1, ListNode(2, ListNode(7))))
l3 = ListNode(3, ListNode(5, ListNode(8, ListNode(9))))
lists = [l1, l2, l3]
result = Solution().mergeKLists(lists)
expected = ListNode(-1, ListNode(0, ListNode(1, ListNode(2, ListNode(3, ListNode(
    3, ListNode(4, ListNode(5, ListNode(7, ListNode(8, ListNode(9)))))))))))
same_values = compare_linked_lists(result, expected)
assert same_values, f"Expected {expected} but got {result}"
