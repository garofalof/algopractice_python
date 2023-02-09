from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        end = 1

        for i in range(end, len(nums)):
            if nums[i] != nums[i-1]:
                nums[end] = nums[i]
                end += 1

        return end

# Explanation:
# -Set end to 1
# -For each index 1 to len of nums:
# -If curr num equal to prev, continue
# -Else set num at index end to curr and increase end by 1
# -Once done, return end

# Notes:
# -Time complexity: O(n)
# -Space complexity: O(1)

uniqueCount = Solution().removeDuplicates([1, 1, 1, 2, 3])

print(f"Unique count is {uniqueCount}")