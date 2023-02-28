from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def two_pointers(nums, i, result):
            start = i + 1
            end = len(nums) - 1

            while start < end:
                total = nums[i] + nums[start] + nums[end]

                if total < 0:
                    start += 1
                elif total > 0:
                    end -= 1
                else:
                    result.append([nums[i], nums[start], nums[end]])
                    start += 1
                    end -= 1

                    while start < end and nums[start] == nums[start - 1]:
                        start += 1

        result = []
        nums.sort()

        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i] != nums[i - 1]:
                two_pointers(nums, i, result)

        return result


"""
Explanation:

This code defines a function threeSum which takes a list of integers nums and returns a list of lists containing all unique triplets in nums which add up to zero. The function uses a helper function two_pointers to efficiently find the triplets.



Initialize an empty list result, sorts the input list nums, and check if the length of nums < 3, in which case return the empty result list as we can't form a triplet. Otherwise, iterate through the sorted nums list and check if the current value at nums[i] > 0. If so, break out of the loop as we can't sum to 0. If i == 0 or the current value at nums[i] != the previous value at nums[i-1], call the two_pointers function to find triplets that add up to zero.

In two_pointers, take a starting index i, and initialize two pointers start and end to the values of i+1 and len(nums)-1, respectively. Then use a while loop to iterate through the list, calculating the sum of nums[i], nums[start], and nums[end]. If the sum < 0, start is incremented by 1, if the sum > 0, end is decremented by 1, and if the sum == 0, the triplet [nums[i], nums[start], nums[end]] is appended to the result list. The start pointer is then incremented and the end pointer is decremented. Finally, check if there are any duplicate values of nums[start] and increment start until the next non-duplicate value is found.

Once done, we return the result list.

Notes:

Time complexity: O(n ^ 2), as we call two_sum, which is O(n), n number of times.

Space complexity: O(log n) to O(n) depending on the implementation of the sorting algorithm.
"""

# Test 1: Min length, triplets add to 0
nums = [-1, 1, 0]
three_sum = Solution().threeSum(nums)
expected = [[-1, 0, 1]]
assert three_sum == expected, f"Expected {expected} but got {three_sum}"

# Test 2: Min length, no triplets add to 0
nums = [1, 2, 3]
three_sum = Solution().threeSum(nums)
expected = []
assert three_sum == expected, f"Expected {expected} but got {three_sum}"

# Test 3: Multiple triplets adding to 0
nums = [-5, -3, -2, -1, 0, 1, 2, 3]
three_sum = Solution().threeSum(nums)
expected = [[-5, 2, 3], [-3, 0, 3], [-3, 1, 2],
            [-2, -1, 3], [-2, 0, 2], [-1, 0, 1]]
assert three_sum == expected, f"Expected {expected} but got {three_sum}"

# Test 4: All negatives
nums = [-5, -4, -3, -2, -1]
three_sum = Solution().threeSum(nums)
expected = []
assert three_sum == expected, f"Expected {expected} but got {three_sum}"

# Test 5: All positives
nums = [1, 2, 3, 4, 5]
three_sum = Solution().threeSum(nums)
expected = []
assert three_sum == expected, f"Expected {expected} but got {three_sum}"
