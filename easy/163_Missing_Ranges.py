from typing import List


class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        result = []
        prev = lower - 1

        for i in range(len(nums) + 1):
            curr = nums[i] if i < len(nums) else upper + 1

            if prev + 1 <= curr - 1:
                formatted = f"{prev + 1}" if prev + \
                    1 == curr - 1 else f"{prev + 1}->{curr - 1}"
                result.append(formatted)

            prev = curr

        return result


"""
Explanation:

Set prev to lower - 1 and initialize an empty result list. Iterate over each number in nums, with an additional iteration for the upper + 1 value. If prev + 1 <= curr - 1, calculate and format the missing range, then append it to the result list. Set prev to curr and repeat the process. Return the result list.

Notes:

Time complexity: O(n)
Space complexity: O(1)
"""

# Test 1: Empty list
nums = []
lower = 0
upper = 99
result = Solution().findMissingRanges(nums, lower, upper)
assert result == ['0->99'], f"Expected ['0->99'], but got {result}"