class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n not in seen:
            seen.add(n)

            n = sum(int(digit) ** 2 for digit in str(n))

            if n == 1:
                return True

        return False


"""
Explanation:

To determine if a number is happy, initialize an empty set called seen to keep track of numbers that have been seen before. Then enter a loop that continues until n is in the seen set. Inside the loop, add the current value of n to the seen set. Then compute the sum of the squares of the digits of n and assign the result back to n. If n equals 1, then it's a happy number and return True. Otherwise, the loop continues. If the loop completes without returning True, return False.

Notes:

Time complexity: O(log n), because the maximum number of iterations needed is proportional to the number of digits in n, which is log10(n), and the maximum sum of squares of digits in n is 81*log10(n).

Space complexity: O(log n), which is a measure of what numbers we're putting in the hashset, and how big they are.
"""

# Test 1: n == 1
n = 1
is_happy = Solution().isHappy(n)
expected = True
assert is_happy == expected, f"Expected {expected} but got {is_happy}"

# Test 2: n > 1, happy
n = 19
is_happy = Solution().isHappy(n)
expected = True
assert is_happy == expected, f"Expected {expected} but got {is_happy}"

# Test 3: n > 1, happy
n = 64
is_happy = Solution().isHappy(n)
expected = False
assert is_happy == expected, f"Expected {expected} but got {is_happy}"

# Test 4: Max value
n = 2 ** 31 - 1
is_happy = Solution().isHappy(n)
expected = False
assert is_happy == expected, f"Expected {expected} but got {is_happy}"
