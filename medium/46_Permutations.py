import math
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        used = set()

        def dfs(memo: List[int]) -> None:
            if len(memo) == len(nums):
                result.append(list(memo))
                return

            for i, num in enumerate(nums):
                if i in used:
                    continue

                curr = num
                used.add(i)
                memo.append(curr)
                dfs(memo)
                memo.pop()
                used.remove(i)

        dfs([])
        return result


"""
Explanation:

Initialize result array to store final permutations and used set to store visited elements. Create a function called dfs which takes memo as input. If the size of memo is equal to the length of nums, push the current permutation to result. For each number in nums, if it's not already in used, add it to memo and used, call the dfs function with the updated memo, and then remove it from memo and used to backtrack. The final result will contain all the permutations.

Notes:

Time Complexity: O(n! * n), since we create a copy of the current permutation every time we find a valid permutation. Since the length of the permutation is n, creating a copy takes O(n) time, and we do this for each of the n! permutations, resulting in a total time complexity of O(n! * n).

Space Complexity: O(n! * n), since we create a new list of length n for each permutation, and there are n! possible permutations. Therefore, the total space required is n! * n. Additionally, we use a set to store the indices of used elements, which requires at most O(n) space. Overall, the space complexity is O(n! * n + n), which simplifies to O(n! * n).
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
