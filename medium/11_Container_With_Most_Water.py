from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_area = 0

        while l < r:
            area = min(height[l], height[r]) * (r - l)
            max_area = max(max_area, area)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return max_area

"""
Explanation:

Initialize left and right index pointers to beginning and end of list. Set max_area to 0. While left pointer < right pointer: calculate current area between left and right pointers. Set max_area to greater of max_area or current area. If left height < right height, increase left pointer. Else decrease right pointer.

Once done, return the max area obtained.

Notes:

Time complexity: O(n), where n is the length of the input list
Space complexity: O(1)
"""

# Test Case 1: General case with increasing heights
heights = [1, 2, 3, 4, 5]
max_area = Solution().maxArea(heights)
expected = 6
assert max_area == expected, f"Expected {expected} but got {max_area}"

# Test Case 2: General case with decreasing heights
heights = [5, 4, 3, 2, 1]
max_area = Solution().maxArea(heights)
expected = 6
assert max_area == expected, f"Expected {expected} but got {max_area}"

# Test Case 3: General case with varied heights
heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]
max_area = Solution().maxArea(heights)
expected = 49
assert max_area == expected, f"Expected {expected} but got {max_area}"

# Test Case 4: Two heights, increasing
heights = [3, 9]
max_area = Solution().maxArea(heights)
expected = 3
assert max_area == expected, f"Expected {expected} but got {max_area}"

# Test Case 5: Two heights, decreasing
heights = [9, 3]
max_area = Solution().maxArea(heights)
expected = 3
assert max_area == expected, f"Expected {expected} but got {max_area}"

# Test Case 6: Maximum constraint, all elements equal
heights = [5] * 105
max_area = Solution().maxArea(heights)
expected = 520
assert max_area == expected, f"Expected {expected} but got {max_area}"

# Test Case 7: Maximum constraint, alternating heights
heights = [i % 2 for i in range(105)]
max_area = Solution().maxArea(heights)
expected = 102
assert max_area == expected, f"Expected {expected} but got {max_area}"
