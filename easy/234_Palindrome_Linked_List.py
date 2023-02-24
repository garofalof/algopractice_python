from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = fast = head

        while fast and fast.next:
            slow, fast = slow.next, fast.next.next

        prev = None

        while slow:
            slow.next, prev, slow = prev, slow, slow.next

        while prev:
            if head.val != prev.val:
                return False

            head, prev = head.next, prev.next

        return True


"""
Explanation:

First find the midpoint of the linked list by iterating through the list with a slow and fast pointer. Then, reverse the second half of the list. Finally, compare the values of the first half with the reversed second half to determine if the linked list is a palindrome or not.

Notes:

Time complexity: O(n), where n is the length of the input list.

Space complexity: O(1), as we use constant space to store pointers.
"""

# Test 1: Single node
list = ListNode(1)
is_palindrome = Solution().isPalindrome(list)
expected = True
assert is_palindrome == expected, f"Expected {expected} but got {is_palindrome}"

# Test 2: Two nodes, valid
list = ListNode(1, ListNode(1))
is_palindrome = Solution().isPalindrome(list)
expected = True
assert is_palindrome == expected, f"Expected {expected} but got {is_palindrome}"

# Test 3: Two nodes, not valid
list = ListNode(1, ListNode(2))
is_palindrome = Solution().isPalindrome(list)
expected = False
assert is_palindrome == expected, f"Expected {expected} but got {is_palindrome}"

# Test 4: Odd number of nodes, valid
list = ListNode(1, ListNode(2, ListNode(1)))
is_palindrome = Solution().isPalindrome(list)
expected = True
assert is_palindrome == expected, f"Expected {expected} but got {is_palindrome}"

# Test 5: Odd number of nodes, not valid
list = ListNode(1, ListNode(2, ListNode(3)))
is_palindrome = Solution().isPalindrome(list)
expected = False
assert is_palindrome == expected, f"Expected {expected} but got {is_palindrome}"

# Test 6: Even number of nodes, valid
list = ListNode(1, ListNode(2, ListNode(2, ListNode(1))))
is_palindrome = Solution().isPalindrome(list)
expected = True
assert is_palindrome == expected, f"Expected {expected} but got {is_palindrome}"

# Test 7: Even number of nodes, not valid
list = ListNode(1, ListNode(2, ListNode(2, ListNode(3))))
is_palindrome = Solution().isPalindrome(list)
expected = False
assert is_palindrome == expected, f"Expected {expected} but got {is_palindrome}"
