import math
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def dfs(nums: List[int], memo: list) -> None:
            if len(memo) == len(nums):
                result.append(list(memo))
                return

            for i in range(len(nums)):
                curr = nums[i]

                if curr in memo:
                    continue

                memo.append(curr)
                dfs(nums, memo)
                memo.pop()

        dfs(nums, [])

        return result


"""
Explanation:

Initialize result array to store final permutations. Create a function called dfs which takes two inputs, nums and memo, where memo is a set that stores the current permutation. If the size of memo is equal to the length of nums, push the current permutation to result. For each number in nums, if it's not already in memo, add it to memo, call the dfs function with the updated memo, and then remove it from memo to backtrack. The final result will contain all the permutations.

Notes:

Time Complexity: O(n * n!), where n is the length of the input array nums. For each element in nums, we have n-1 choices, so the time complexity is dominated by the number of permutations, which is n!.

Space Complexity: O(n * n!), where n is the length of the input array nums. The space complexity is proportional to the number of permutations, which is n!, because we need to store all the permutations.
"""

# Test 1: Single element
nums = [1]
result = Solution().permute(nums)
result_len = len(result) == len(nums)
same_inner_len = all(len(p) == len(nums) for p in result)
unique_inner_nums = all(set(p) == set(nums) for p in result)
assert result_len, f"Expected same_outer_len to equal True but got {result_len}"
assert same_inner_len, f"Expected same_inner_len to equal True but got {same_inner_len}"
assert unique_inner_nums, f"Expected unique_inner_nums to equal True but got {unique_inner_nums}"

# Test 2: Two elements
nums = [1, 2]
result = Solution().permute(nums)
result_len = len(result) == len(nums)
same_inner_len = all(len(p) == len(nums) for p in result)
unique_inner_nums = all(set(p) == set(nums) for p in result)
assert result_len, f"Expected same_outer_len to equal True but got {result_len}"
assert same_inner_len, f"Expected same_inner_len to equal True but got {same_inner_len}"
assert unique_inner_nums, f"Expected unique_inner_nums to equal True but got {unique_inner_nums}"

# Test 2: Greater than two elements
nums = [1, 2, 3]
result = Solution().permute(nums)
same_inner_len = all(len(p) == len(nums) for p in result)
unique_inner_nums = all(set(p) == set(nums) for p in result)
assert len(result) == math.factorial(
    len(nums)), f"Expected 6 but got {len(result)}"
assert same_inner_len, f"Expected same_inner_len to equal True but got {same_inner_len}"
assert unique_inner_nums, f"Expected unique_inner_nums to equal True but got {unique_inner_nums}"

# Test 3: Max elements
nums = [1, 2, 3, 4, 5, 6]
result = Solution().permute(nums)
same_inner_len = all(len(p) == len(nums) for p in result)
unique_inner_nums = all(set(p) == set(nums) for p in result)
assert len(result) == math.factorial(
    len(nums)), f"Expected 720 but got {len(result)}"
assert same_inner_len, f"Expected same_inner_len to equal True but got {same_inner_len}"
assert unique_inner_nums, f"Expected unique_inner_nums to equal True but got {unique_inner_nums}"
