class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, node):
        node.val, node.next = node.next.val, node.next.next


"""
Explanation:

To delete a node from a linked list, we don't actually remove the node itself. Instead, we replace the node's value with the value of the next node and rearrange the pointers to skip over the next node. This effectively "deletes" the node by bypassing it and making it inaccessible from the linked list.

Notes:

Time complexity: O(1)

Space complexity: O(1)
"""


def linked_list_to_list(head):
    result = []
    node = head
    while node:
        result.append(node.val)
        node = node.next
    return result

# Test Case 1: Deleting the middle node
head = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
head.next = node2
node2.next = node3
node3.next = node4
Solution().deleteNode(node2)
expected_result = [1, 3, 4]
assert linked_list_to_list(head) == expected_result, f"Expected {expected_result} but got {linked_list_to_list(head)}"

# Test Case 2: Deleting the first node
head = ListNode(5)
node7 = ListNode(7)
node8 = ListNode(8)
node9 = ListNode(9)
head.next = node7
node7.next = node8
node8.next = node9
Solution().deleteNode(head)
expected_result = [7, 8, 9]
assert linked_list_to_list(head) == expected_result, f"Expected {expected_result} but got {linked_list_to_list(head)}"

# Test Case 3: Deleting the second node
head = ListNode(10)
node20 = ListNode(20)
node30 = ListNode(30)
node40 = ListNode(40)
head.next = node20
node20.next = node30
node30.next = node40
Solution().deleteNode(node20)
expected_result = [10, 30, 40]
assert linked_list_to_list(head) == expected_result, f"Expected {expected_result} but got {linked_list_to_list(head)}"

# Test Case 4: Deleting the second-to-last node
head = ListNode(100)
node200 = ListNode(200)
node300 = ListNode(300)
node400 = ListNode(400)
head.next = node200
node200.next = node300
node300.next = node400
Solution().deleteNode(node300)
expected_result = [100, 200, 400]
assert linked_list_to_list(head) == expected_result, f"Expected {expected_result} but got {linked_list_to_list(head)}"
