from typing import List


class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        result = []
        prev = lower - 1

        nums.append(upper + 1)

        for i in range(len(nums)):
            low = prev + 1
            high = nums[i] - 1

            if low <= high:
                result.append(f"{low}" if low == high else f"{low}->{high}")

            prev = nums[i]

        return result


"""
Explanation:

Set variable prev to lower - 1 and initialize an empty result list. Add upper + 1 to end of nums list. Iterate over each number in nums. If prev + 1 <= curr - 1, calculate and format the missing range, then append it to the result list. Set prev to curr and repeat the process. Return the result list.

Notes:

Time complexity: O(n)
Space complexity: O(1)
"""

# Test 1: Multiple elements w/ missing ranges
nums = [0, 1, 3, 50, 75]
lower = 0
upper = 99
result = Solution().findMissingRanges(nums, lower, upper)
assert result == [
    "2", "4->49", "51->74", "76->99"], f"Expected['2', '4->49', '51->74', '76->99'] but got {result}"

# Test 2: Multiple elements w/ no missing ranges
nums = [1, 2, 3, 4, 5]
lower = 1
upper = 5
result = Solution().findMissingRanges(nums, lower, upper)
assert result == [], f"Expected [] but got {result}"

# Test 3: Single element w/ missing ranges
nums = [1]
lower = -1
upper = 100
result = Solution().findMissingRanges(nums, lower, upper)
assert result == [
    "-1->0", "2->100"], f"Expected ['-1->0', '2->100'] but got {result}"

# Test 4: Single element same as low/high bounds
nums = [1]
lower = 1
upper = 1
result = Solution().findMissingRanges(nums, lower, upper)
assert result == [], f"Expected [] but got {result}"

# Test 5: Missing ranges of size one
nums = [1, 3, 5, 7, 9]
lower = 0
upper = 10
result = Solution().findMissingRanges(nums, lower, upper)
assert result == [
    "0", "2", "4", "6", "8", "10"], f"Expected ['0', '2', '4', '6', '8', '10'] but got {result}"
