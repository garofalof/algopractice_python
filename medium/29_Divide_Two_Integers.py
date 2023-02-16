class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = (dividend > 0) == (divisor > 0)
        dividend, divisor = abs(dividend), abs(divisor)
        result = 0

        while dividend >= divisor:
            temp, multiple = divisor, 1

            while dividend >= temp:
                dividend -= temp
                result += multiple
                multiple *= 2
                temp *= 2

        return min(result if sign else -result, 2**31-1)


"""
Explanation:

Determine the sign of the result by checking if the signs of the dividend and divisor are the same. Take the absolute value of the inputs, since we only need to work with positive integers. Then, repeatedly subtract the divisor from the dividend until the dividend is less than the divisor. Keep track of how many times the divisor was subtracted (the "multiple") and double the multiple and the divisor in each iteration.

Finally, return the result, taking into account the sign of the inputs, and ensuring that the result does not exceed the range of a 32-bit signed integer (between -2^31 and 2^31-1).

Notes:

Time complexity: O(log n), where n is the absolute value of the dividend, because the algorithm divides the dividend by a factor of 2 with each iteration of the inner while loop.

Space complexity: O(1), because the amount of memory the algorithm needs to use stays constant regardless of the size of the input.
"""

# Test 1: Dividend min value, divisor 1
d = -2 ** 31
dv = 1
result = Solution().divide(d, dv)
expected = -2 ** 31
assert result == expected, f"Expected {expected} but got {result}"

# Test 2: Dividend max value, divisor 1
d = 2 ** 31 - 1
dv = 1
result = Solution().divide(d, dv)
expected = 2 ** 31 - 1
assert result == expected, f"Expected {expected} but got {result}"

# Test 3: Dividend 1, divisor min value
d = 1
dv = -2 ** 31
result = Solution().divide(d, dv)
expected = 0
assert result == expected, f"Expected {expected} but got {result}"

# Test 4: Dividend 1, divisor max value
d = 1
dv = 2 ** 31
result = Solution().divide(d, dv)
expected = 0
assert result == expected, f"Expected {expected} but got {result}"

# Test 5: Same sign, no remainder
d = 35
dv = 7
result = Solution().divide(d, dv)
expected = 5
assert result == expected, f"Expected {expected} but got {result}"

# Test 6: Same sign, remainder
d = 35
dv = 6
result = Solution().divide(d, dv)
expected = 5
assert result == expected, f"Expected {expected} but got {result}"

# Test 7: Diff sign, no remainder
d = -35
dv = 7
result = Solution().divide(d, dv)
expected = -5
assert result == expected, f"Expected {expected} but got {result}"

# Test 8: Diff sign, remainder
d = -35
dv = 6
result = Solution().divide(d, dv)
expected = -5
assert result == expected, f"Expected {expected} but got {result}"
