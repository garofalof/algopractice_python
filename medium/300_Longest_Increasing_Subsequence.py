from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)

        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)


"""
Explanation:

Initialize dp with all 1's since each element is itself a valid increasing subsequence of length 1. Then loop through the elements of the array from left to right, and for each element nums[i], compare it to all the previous elements nums[j] with indices j less than i. If nums[i] > nums[j], extend the increasing subsequence that ends at j by including nums[i] at the end. In this case, update dp[i] to be the max of its current value and dp[j] + 1, which is the length of the subsequence that ends at j + 1. After looping through all the elements of the array, the length of the longest increasing subsequence will be the max value in the dp array, so return max(dp).

Notes:

Time complexity: O(n ^ 2), where n is the length of the input sequence, since we use a nested loop to compare each pair of elements.

Space complexity: O(n), as we use extra space of size n for the dp array.
"""

# Test 1: Single element
nums = [1]
longest_increasing = Solution().lengthOfLIS(nums)
expected = 1
assert longest_increasing == expected, f"Expected {expected} but got {longest_increasing}"

# Test 2: Sorted array
nums = [1, 10, 17, 24, 32]
longest_increasing = Solution().lengthOfLIS(nums)
expected = 5
assert longest_increasing == expected, f"Expected {expected} but got {longest_increasing}"

# Test 3: Reverse sorted array
nums = [27, 14, 11, 9, 5]
longest_increasing = Solution().lengthOfLIS(nums)
expected = 1
assert longest_increasing == expected, f"Expected {expected} but got {longest_increasing}"

# Test 4: Random array
nums = [3, 27, 14, 91, 52, 4]
longest_increasing = Solution().lengthOfLIS(nums)
expected = 3
assert longest_increasing == expected, f"Expected {expected} but got {longest_increasing}"

# Test 5: Array w/ repeating elements
nums = [1, 1, 1, 1, 1]
longest_increasing = Solution().lengthOfLIS(nums)
expected = 1
assert longest_increasing == expected, f"Expected {expected} but got {longest_increasing}"

# Test 6: Array w/ positive and negative numbers
nums = [1, -11, -14, 3, 7]
longest_increasing = Solution().lengthOfLIS(nums)
expected = 3
assert longest_increasing == expected, f"Expected {expected} but got {longest_increasing}"
