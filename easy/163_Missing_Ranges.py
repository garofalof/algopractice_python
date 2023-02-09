from typing import List


class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        result = []
        prev = lower - 1

        for i in range(len(nums) + 1):
            curr = nums[i] if i < len(nums) else upper + 1

            if prev + 1 <= curr - 1:
                formatted = f"{prev + 1}" if prev + 1 == curr - 1 else f"{prev + 1}->{curr - 1}"
                result.append(formatted)

            prev = curr

        return result

# Explanation:
# -Set result to empty array and prev to lower - 1
# -For each num in nums:
# -Set curr to num at curr index if index within nums, else set to upper + 1
# -If diff between prev and curr > 1, push formatted range to result
# -Then set prev to curr and continue
# -Once done, return result

# Notes:
# -Time complexity: O(n)
# -Space complexity: O(1), as we don't count output array as extra space

missing = Solution().findMissingRanges([0, 1, 3, 50, 75], 0, 99)

print(f"Missing ranges are {missing}")