from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr, carry = dummy, 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            carry, val = divmod(val1 + val2 + carry, 10)
            curr.next = ListNode(val)

            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next


"""
Explanation:

Create a dummy node with value of 0 to serve as a placeholder for the sum of the two input linked lists. Create two pointers curr and carry to keep track of the current sum and any carry-over from the previous sum. Iterate over the linked lists using a while loop, adding the values of the two nodes and the carry value if it exists. Update carry to be the integer division of the sum by 10, and set val to be the remainder of the division. Create a new ListNode with val, set it as the next node for curr, and update curr to point to the new node. Move l1 and l2 to their next nodes if they exist. Once done, return the dummy pointer's next node as the sum of the linked lists.

Notes:

Time Complexity: O(max(n,m)), where n and m are the lengths of the two linked lists. We traverse the length of the longer linked list, so in the worst case the time complexity is proportional to the length of the longer list.

Space Complexity: O(max(n,m)), where n and m are the lengths of the two linked lists. We create a new linked list of length max(n,m) to hold the sum, so the space complexity is proportional to the length of the longer list.
"""

# Test 1: Single numbers w/ sum < 10
l1 = ListNode(3)
l2 = ListNode(4)
sum_list = Solution().addTwoNumbers(l1, l2)
sum = 0
expected = 7

while sum_list:
    sum = sum * 10 + sum_list.val
    sum_list = sum_list.next

assert sum == expected, f"Expected {expected} but got {sum}"

# Test 2: Single numbers w/ sum > 10
l1 = ListNode(7)
l2 = ListNode(4)
sum_list = Solution().addTwoNumbers(l1, l2)
sum = 0
expected = 11

while sum_list:
    sum = sum * 10 + sum_list.val
    sum_list = sum_list.next

assert sum == expected, f"Expected {expected} but got {sum}"

# Test 3: Multiple nums w/ sum < 10, same length
l1 = ListNode(1, ListNode(2, ListNode(3)))
l2 = ListNode(4, ListNode(5, ListNode(6)))
sum_list = Solution().addTwoNumbers(l1, l2)
sum = 0
expected = 579

while sum_list:
    sum = sum * 10 + sum_list.val
    sum_list = sum_list.next

assert sum == expected, f"Expected {expected} but got {sum}"

# Test 4: Multiple nums w/ sum < 10, different lengths
l1 = ListNode(1, ListNode(2))
l2 = ListNode(4, ListNode(5, ListNode(6)))
sum_list = Solution().addTwoNumbers(l1, l2)
sum = 0
expected = 576

while sum_list:
    sum = sum * 10 + sum_list.val
    sum_list = sum_list.next

assert sum == expected, f"Expected {expected} but got {sum}"

# Test 5: Multiple nums w/ sum > 10, same length
l1 = ListNode(1, ListNode(2, ListNode(3)))
l2 = ListNode(5, ListNode(9, ListNode(1)))
sum_list = Solution().addTwoNumbers(l1, l2)
sum = 0
expected = 615

while sum_list:
    sum = sum * 10 + sum_list.val
    sum_list = sum_list.next

assert sum == expected, f"Expected {expected} but got {sum}"

# Test 6: Multiple nums w/ sum > 10, different lengths
l1 = ListNode(1, ListNode(2))
l2 = ListNode(5, ListNode(9, ListNode(1)))
sum_list = Solution().addTwoNumbers(l1, l2)
sum = 0
expected = 612

while sum_list:
    sum = sum * 10 + sum_list.val
    sum_list = sum_list.next

assert sum == expected, f"Expected {expected} but got {sum}"

# Test 7: Multiple nums w/ carry in last digit
l1 = ListNode(9, ListNode(9, ListNode(9)))
l2 = ListNode(9, ListNode(9, ListNode(9)))
sum_list = Solution().addTwoNumbers(l1, l2)
sum = 0
expected = 8991

while sum_list:
    sum = sum * 10 + sum_list.val
    sum_list = sum_list.next

assert sum == expected, f"Expected {expected} but got {sum}"
