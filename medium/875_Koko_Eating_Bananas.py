import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        while l <= r:
            k = (r - l) // 2 + l
            hours = sum(math.ceil(pile / k) for pile in piles)

            if hours <= h:
                r = k - 1
            else:
                l = k + 1

        return l


"""
Explanation:

Start by setting the left pointer l to 1 and the right pointer r to the maximum value in the piles list. Then, enter a while loop and compute the midpoint k between l and r. Then calculate the total number of hours it would take to eat all the piles at the current eating speed k.

If the total hours <= the maximum number of hours h, it means that the current eating speed is too slow or just right, so the right pointer is moved left to k-1 to check if a slower eating speed is possible. Otherwise, if the total hours > h, the current eating speed is too fast, so the left pointer is moved right to k+1 to check if a faster eating speed is possible.

This process is repeated until the left and right pointers converge, at which point we return the left pointer l, which represents the minimum eating speed needed to eat all the piles within h hours.

Notes:

Time complexity: O(n log m), where n is the length of input list piles and m is the max pile in the input list.

Space complexity: O(1), as we use constant extra space to store pointers l, r, k, and hours.
"""

# Test 1: Minimum input
piles = [1]
h = 1
min_speed = Solution().minEatingSpeed(piles, h)
expected = 1
assert min_speed == expected, f"Expected {expected} but got {min_speed}"

# Test 2: Speed == max pile
piles = [1, 2, 3, 4, 5]
h = 5
min_speed = Solution().minEatingSpeed(piles, h)
expected = 5
assert min_speed == expected, f"Expected {expected} but got {min_speed}"

# Test 3: All piles same value
piles = [3] * 5
h = 3
min_speed = Solution().minEatingSpeed(piles, h)
expected = 4
assert min_speed == expected, f"Expected {expected} but got {min_speed}"

# Test 4: Speed > max pile
piles = [1, 2, 3, 4, 5]
h = 8
min_speed = Solution().minEatingSpeed(piles, h)
expected = 3
assert min_speed == expected, f"Expected {expected} but got {min_speed}"

# Test 5: Decreasing values
piles = [5, 4, 3, 2, 1]
h = 3
min_speed = Solution().minEatingSpeed(piles, h)
expected = 6
assert min_speed == expected, f"Expected {expected} but got {min_speed}"

# Test 6: Random values, large speed
piles = [5, 3, 1, 10, 7]
h = 30
min_speed = Solution().minEatingSpeed(piles, h)
expected = 1
assert min_speed == expected, f"Expected {expected} but got {min_speed}"

# Test 7: Very large speed
piles = [5, 3, 1, 10, 7]
h = 1000000000
min_speed = Solution().minEatingSpeed(piles, h)
expected = 1
assert min_speed == expected, f"Expected {expected} but got {min_speed}"
