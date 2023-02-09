from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        end = 1

        for i in range(end, len(nums)):
            if nums[i] != nums[i-1]:
                nums[end] = nums[i]
                end += 1

        return end

"""
Explanation:

The code implements a solution to remove duplicates from a list of integers and return the count of unique elements. It uses two variables end and i to traverse the list and keep track of the end of the unique elements. If the current element is not equal to the previous element, it is added to the end of the unique elements and the end variable is incremented by 1. The code returns the value of end, which is the count of unique elements in the list.

Notes:

Time complexity: O(n), where n is the length of the list nums
Space complexity: O(1), because the code modifies the input list in-place and only uses a constant amount of extra memory
"""

# Test 1: Single element in list
nums = [1]
unique_count = Solution().removeDuplicates(nums)
assert unique_count == 1

# Test 2: No duplicates
nums = [1, 2, 3, 4, 5]
unique_count = Solution().removeDuplicates(nums)
assert unique_count == 5

# Test 3: All duplicates
nums = [1, 1, 1, 1, 1]
unique_count = Solution().removeDuplicates(nums)
assert unique_count == 1

# Test 4: Some duplicates
nums = [1, 2, 2, 3, 3, 4, 4, 4, 5, 5, 5, 5, 5]
unique_count = Solution().removeDuplicates(nums)
assert unique_count == 5