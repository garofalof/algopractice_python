from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        curr, prev = head, dummy

        def reverseNodes(node, k):
            curr, prev = node, None

            for _ in range(k):
                curr.next, prev, curr = prev, curr, curr.next

            return prev

        while curr:
            tail, count = curr, 0

            while curr and count < k:
                curr = curr.next
                count += 1
            if count == k:
                prev.next = reverseNodes(tail, k)
                prev = tail
            else:
                prev.next = tail

        return dummy.next


"""
Explanation:

Create a dummy node and set its next pointer to the head of the given linked list. Initialize prev and curr pointers to the dummy node and the head, respectively. Then iterate through the linked list using the curr pointer. Inside the loop, set tail as the current node and count as 0. These variables help us keep track of the k-group of nodes that need to be reversed. Continue moving the curr pointer and incrementing the count until we reach the end of the linked list or count becomes equal to k. If count == k, it means we have a complete k-group of nodes to reverse. Update the next pointers of the nodes in the k-group to reverse their order using the reverseNodes method. Update the next pointer of prev to the new head of the reversed k-group. Move prev to the last node in the reversed k-group, which becomes the new prev for the next iteration. If count < k, it means we have reached the end of the linked list without a complete k-group. We simply connect prev to the remaining nodes and break out of the loop.

Finally, return the next pointer of the dummy node, which points to the head of the modified linked list.

Notes:

Time complexity: O(n)

Space complexity: O(1)
"""


def linked_list_to_list(head):
    result = []

    while head:
        result.append(head.val)
        head = head.next

    return result


# Test Case 1: Single node, k == 1
head = ListNode(0)
k = 1
result = linked_list_to_list(Solution().reverseKGroup(head, k))
expected = linked_list_to_list(ListNode(0))
assert result == expected, f"Expected {expected} but got {result}"

# Test Case 2: List length == k
head = ListNode(1, ListNode(2, ListNode(3)))
k = 3
result = linked_list_to_list(Solution().reverseKGroup(head, k))
expected = linked_list_to_list(ListNode(3, ListNode(2, ListNode(1))))
assert result == expected, f"Expected {expected} but got {result}"

# Test Case 3: List length > k
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
k = 3
result = linked_list_to_list(Solution().reverseKGroup(head, k))
expected = linked_list_to_list(
    ListNode(3, ListNode(2, ListNode(1, ListNode(4, ListNode(5))))))
assert result == expected, f"Expected {expected} but got {result}"

# Test Case 4: List length multiple of k
head = ListNode(1, ListNode(2, ListNode(
    3, ListNode(4, ListNode(5, ListNode(6))))))
k = 2
result = linked_list_to_list(Solution().reverseKGroup(head, k))
expected = linked_list_to_list(ListNode(2, ListNode(
    1, ListNode(4, ListNode(3, ListNode(6, ListNode(5)))))))
assert result == expected, f"Expected {expected} but got {result}"
