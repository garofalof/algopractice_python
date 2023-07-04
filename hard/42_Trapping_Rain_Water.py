from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        result = 0

        while left < right:
            if right_max > left_max:
                left += 1
                left_max = max(left_max, height[left])
                result += left_max - height[left]
            else:
                right -= 1
                right_max = max(right_max, height[right])
                result += right_max - height[right]

        return result


"""
Explanation:

Check if the height list is empty. If it is, there are no bars, so the trapped water is 0.

Initialize two pointers, left and right, at the start and end of the height list, respectively. Initialize two variables, left_max and right_max, to track the max height encountered on the left and right sides, starting with the heights of the first and last bars. Initialize a variable result to keep track of the total trapped water.

While left and right haven't met, compare the right_max and left_max heights. If right_max > left_max, it means there's a potential trap on the left side. The left pointer is moved one step to the right, and the new bar's height is compared with the left_max. The trapped water is then calculated by subtracting the current bar's height from the left_max, and the result is added to the total trapped water. If right_max is not greater than left_max, there's a potential trap on the right side. The right pointer is moved one step to the left, and the new bar's height is compared with the right_max. The trapped water is calculated similarly to the left side. The loop continues until the left and right pointers meet, at which point all potential traps have been accounted for.

Finally, return the result, which represents the total amount of water trapped between the bars.

Notes:

Time complexity: O(n), where n is the number of bars in the height list

Space complexity: O(1), as the algorithm only uses a constant amount of extra space to store variables
"""

# Test Case 1: Single bar
height = [1]
result = Solution().trap(height)
expected = 0
assert result == expected, f"Expected {expected} but got {result}"

# Test Case 2: No bars
height = [0, 0, 0]
result = Solution().trap(height)
expected = 0
assert result == expected, f"Expected {expected} but got {result}"

# Test Case 3: No trapped water
height = [1, 2, 3, 4, 5]
result = Solution().trap(height)
expected = 0
assert result == expected, f"Expected {expected} but got {result}"

# Test Case 4: Trapped water between bars
height = [4, 2, 0, 3, 2, 5]
result = Solution().trap(height)
expected = 9
assert result == expected, f"Expected {expected} but got {result}"

# Test Case 5: Varying bar heights
height = [3, 0, 1, 3, 0, 5]
result = Solution().trap(height)
expected = 8
assert result == expected, f"Expected {expected} but got {result}"

# Test Case 6: All bars have equal heights
height = [3, 3, 3, 3, 3]
result = Solution().trap(height)
expected = 0
assert result == expected, f"Expected {expected} but got {result}"

# Test Case 7: Bars in descending order
height = [5, 4, 3, 2, 1]
result = Solution().trap(height)
expected = 0
assert result == expected, f"Expected {expected} but got {result}"

# Test Case 8: Random heights
height = [1, 0, 3, 2, 4, 1, 2]
result = Solution().trap(height)
expected = 3
assert result == expected, f"Expected {expected} but got {result}"
