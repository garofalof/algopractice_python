from typing import List


class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        sum_map = {}
        count = 0

        for n1 in nums1:
            for n2 in nums2:
                total = sum([n1, n2])
                sum_map[total] = sum_map.get(total, 0) + 1
        for n3 in nums3:
            for n4 in nums4:
                total = -sum([n3, n4])
                count += sum_map.get(total, 0)

        return count


"""
Explanation:

Use a dictionary called sum_map to store the number of times a particular sum occurs between nums1 and nums2. Then, iterate through nums3 and nums4, and for each pair of numbers, calculate the negative sum of the pair. If the negative sum is present in sum_map, then increment the count by the number of times that sum occurs in sum_map.

The logic behind this approach is that if a + b = x and c + d = -x, then a + b + c + d = 0. By using a hash table to store the counts of sums of elements from nums1 and nums2, we can quickly check if the negative sum of any pair of elements from nums3 and nums4 is present in the hash table, and increment the count by the number of times that sum occurs in the hash table.

Notes:

Time complexity: O(n ^ 2), as we iterate through two lists of n elements each.

Space complexity: O(n ^ 2), as we store a hash table of n ^ 2 sums in the worst case.
"""


# Test 1: Single digits, sum pairs exist
nums1 = [1]
nums2 = [2]
nums3 = [-2]
nums4 = [-1]
count = Solution().fourSumCount(nums1, nums2, nums3, nums4)
expected = 1
assert count == expected, f"Expected {expected} but got {count}"

# Test 2: Single digits, no sum pairs exist
nums1 = [1]
nums2 = [2]
nums3 = [-3]
nums4 = [1]
count = Solution().fourSumCount(nums1, nums2, nums3, nums4)
expected = 0
assert count == expected, f"Expected {expected} but got {count}"

# Test 3: All same
nums1 = [1]
nums2 = [1]
nums3 = [1]
nums4 = [1]
count = Solution().fourSumCount(nums1, nums2, nums3, nums4)
expected = 0
assert count == expected, f"Expected {expected} but got {count}"

# Test 4: All positives
nums1 = [1, 3]
nums2 = [1, 2]
nums3 = [2, 1]
nums4 = [0, 2]
count = Solution().fourSumCount(nums1, nums2, nums3, nums4)
expected = 0
assert count == expected, f"Expected {expected} but got {count}"

# Test 5: All negatives
nums1 = [-1, -3]
nums2 = [-1, -2]
nums3 = [-2, -1]
nums4 = [0, -2]
count = Solution().fourSumCount(nums1, nums2, nums3, nums4)
expected = 0
assert count == expected, f"Expected {expected} but got {count}"

# Test 6: Mix of positives and negatives add to sum pair
nums1 = [-1, 3]
nums2 = [1, 2]
nums3 = [-2, -1]
nums4 = [0, -2]
count = Solution().fourSumCount(nums1, nums2, nums3, nums4)
expected = 2
assert count == expected, f"Expected {expected} but got {count}"
