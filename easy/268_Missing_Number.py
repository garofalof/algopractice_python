from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        expected_sum = n * (n + 1) // 2
        actual_sum = sum(nums)

        return expected_sum - actual_sum


"""
Explanation:

Compute the expected sum of the sequence of integers from 0 to n using the formula n * (n + 1) / 2, and store the result in the variable expected_sum. The expected_sum formula is derived from the fact that the sum of an arithmetic sequence is given by n * (a_1 + a_n) / 2, where n is the number of terms and a_1 and a_n are the first and last terms of the sequence, respectively. In this case, the first term is 0 and the last term is n, so the sum is n * (n + 1) / 2. Compute the actual sum of the numbers in the input list using the sum function, and store the result in the variable actual_sum. Subtract the actual sum from the expected sum and return the difference, which is the missing number in the sequence.

Notes:

Time complexity: O(n), as we need to iterate over the entire input list to compute the actual sum.

Space complexity: O(1), as we only need to store a few variables to compute the expected and actual sums.
"""

# Test 1: n == 1, missing 0
nums = [1]
missing_num = Solution().missingNumber(nums)
expected = 0
assert missing_num == expected, f"Expected {expected} but got {missing_num}"

# Test 2: n == 1, missing 1
nums = [0]
missing_num = Solution().missingNumber(nums)
expected = 1
assert missing_num == expected, f"Expected {expected} but got {missing_num}"

# Test 3: Missing number beginning of sequence
nums = [1, 2, 3]
missing_num = Solution().missingNumber(nums)
expected = 0
assert missing_num == expected, f"Expected {expected} but got {missing_num}"

# Test 4: Missing number middle of sequence
nums = [0, 1, 3]
missing_num = Solution().missingNumber(nums)
expected = 2
assert missing_num == expected, f"Expected {expected} but got {missing_num}"

# Test 5: Missing number end of sequence
nums = [0, 1, 2]
missing_num = Solution().missingNumber(nums)
expected = 3
assert missing_num == expected, f"Expected {expected} but got {missing_num}"

# Test 6: Missing number in randomized list
nums = [4, 1, 0, 2]
missing_num = Solution().missingNumber(nums)
expected = 3
assert missing_num == expected, f"Expected {expected} but got {missing_num}"
