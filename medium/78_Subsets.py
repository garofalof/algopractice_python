from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        self.dfs([], 0, result, nums)

        return result

    def dfs(self, memo: List[int], start: int, result: List[int], nums: List[int]) -> List[List[int]]:
        result.append(memo[:])

        for i in range(start, len(nums)):
            memo.append(nums[i])
            self.dfs(memo, i + 1, result, nums)
            memo.pop()

"""
Explanation:

Initialize an empty list result to store the subsets. Call the dfs method, passing an empty list [] as the initial subset, index 0 as the starting point, and the result list and nums list as parameters. In the dfs method: append a copy of the current subset memo to the result list. This adds the current subset to the list of subsets. Iterate through the remaining elements in the nums list, starting from the given start index. Add the current element to the subset memo by appending it. Recursively call the dfs method with the updated memo, i + 1 as the new starting index, and the result list and nums list. After the recursive call, remove the last element from the subset memo by popping it. This allows backtracking and exploring other possibilities.

Finally, return the result list, which contains all possible subsets of nums.

Notes:

Time complexity: O(2^n * n), where n is the length of the nums list. This is because there are 2^n possible subsets, and for each subset, we need to make a copy of the current subset memo before appending it to the result list, which takes O(n) time.

Space complexity: O(n) on the recursion stack
"""

# Test Case 1: Single element
nums = [1]
result = Solution().subsets(nums)
expected = [[], [1]]
assert result == expected, f"Expected {expected} but got {result}"

# Test Case 2: Two elements
nums = [1, 2]
result = Solution().subsets(nums)
expected = [[], [1], [1, 2], [2]]
assert result == expected, f"Expected {expected} but got {result}"

# Test Case 3: Three elements
nums = [1, 2, 3]
result = Solution().subsets(nums)
expected = [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
assert result == expected, f"Expected {expected} but got {result}"

# Test Case 4: Positives and negatives
nums = [1, -1]
result = Solution().subsets(nums)
expected = [[], [1], [1, -1], [-1]]
assert result == expected, f"Expected {expected} but got {result}"

# Test Case 5: All negatives
nums = [-1, -2]
result = Solution().subsets(nums)
expected = [[], [-1], [-1, -2], [-2]]
assert result == expected, f"Expected {expected} but got {result}"