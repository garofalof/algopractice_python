class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 1, x
        result = 0

        while l <= r:
            mid = (r - l) // 2 + l
            mid_squared = mid ** 2

            if mid_squared <= x:
                result = mid
                l = mid + 1
            else:
                r = mid - 1

        return result


"""
Explanation:

Implement a binary search algorithm to find the square root of a given non-negative integer x. Initialize the search range to be [1, x] and use the midpoint to divide the search range in each iteration. If the square of the midpoint <= x, update the result to be the midpoint and move the left pointer to mid + 1. If the square of the midpoint > x, move the right pointer to mid - 1. Continue until the left pointer exceeds the right pointer. The final result is the last midpoint that was found.

Notes:

Time complexity: O(log n), since we are performing a binary search to find the square root of n.

Space complexity: O(1), since we are only using a constant amount of extra space to store variables.
"""

# Test 1: x == 0
x = 0
square_root = Solution().mySqrt(x)
expected = 0
assert square_root == expected, f"Expected {expected} but got {square_root}"

# Test 2: x == 1
x = 1
square_root = Solution().mySqrt(x)
expected = 1
assert square_root == expected, f"Expected {expected} but got {square_root}"

# Test 3: x == 2
x = 2
square_root = Solution().mySqrt(x)
expected = 1
assert square_root == expected, f"Expected {expected} but got {square_root}"

# Test 4: x == 4
x = 4
square_root = Solution().mySqrt(x)
expected = 2
assert square_root == expected, f"Expected {expected} but got {square_root}"

# Test 5: x == max value
x = 2 ** 31 - 1
square_root = Solution().mySqrt(x)
expected = 46340
assert square_root == expected, f"Expected {expected} but got {square_root}"
