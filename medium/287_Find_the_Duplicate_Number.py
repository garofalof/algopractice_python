from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = nums[0]

        while True:
            slow, fast = nums[slow], nums[nums[fast]]

            if slow == fast:
                break

        slow = nums[0]

        while slow != fast:
            slow, fast = nums[slow], nums[fast]

        return slow


"""
Explanation:

Initialize two variables slow and fast to the first element of nums. Then enter a loop that continues until it finds a cycle in the list using Floyd's cycle-finding algorithm. On each iteration, slow is moved one step ahead in the list, while fast is moved two steps ahead. If there is a cycle in the list, the two pointers will eventually meet.

Once a cycle has been detected, slow is reset to the first element of the list, while fast remains at the meeting point. We then enter another loop that continues until slow and fast meet at the duplicate number. On each iteration, both pointers are moved one step ahead in the list. When they meet, the duplicate number has been found and is returned.

Notes:

Time complexity: O(n), as we use two loop that run at most n times.

Space complexity: O(1), as we use constant extra space for the slow and fast pointers.
"""

# Test 1: Single element / duplicate
nums = [1, 1]
duplicate = Solution().findDuplicate(nums)
expected = 1
assert duplicate == expected, f"Expected {expected} but got {duplicate}"

# Test 2: Multiple elements, duplicate in beginning
nums = [1, 1, 2, 3, 4]
duplicate = Solution().findDuplicate(nums)
expected = 1
assert duplicate == expected, f"Expected {expected} but got {duplicate}"

# Test 3: Multiple elements, duplicate in middle
nums = [1, 2, 1, 3, 4]
duplicate = Solution().findDuplicate(nums)
expected = 1
assert duplicate == expected, f"Expected {expected} but got {duplicate}"

# Test 4: Multiple elements, duplicate in end
nums = [1, 2, 3, 4, 1]
duplicate = Solution().findDuplicate(nums)
expected = 1
assert duplicate == expected, f"Expected {expected} but got {duplicate}"

# Test 5: Randomized list w/ duplicate
nums = [4, 2, 1, 3, 1]
duplicate = Solution().findDuplicate(nums)
expected = 1
assert duplicate == expected, f"Expected {expected} but got {duplicate}"

# Test 6: Repeating duplicate
nums = [1, 1, 1, 1, 2, 3, 4]
duplicate = Solution().findDuplicate(nums)
expected = 1
assert duplicate == expected, f"Expected {expected} but got {duplicate}"
