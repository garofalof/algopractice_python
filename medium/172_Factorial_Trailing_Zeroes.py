class Solution:
    def trailingZeroes(self, n: int) -> int:
        zeroes = 0

        while n:
            n //= 5
            zeroes += n

        return zeroes


"""
Explanation:

The variable zeroes is initialized to zero.

A while loop is executed as long as n is not 0. The loop calculates the number of factors of 5 in n! by dividing n by 5 and adding the result to zeroes. This is done because a trailing zero in n! is formed whenever there is a factor of 10, which requires a factor of 5 and a factor of 2. Since there are always more factors of 2 than 5, we only need to count the number of factors of 5 to get the number of trailing zeros.

The loop continues to divide n by 5 and add the result to zeroes until n becomes less than 5. At this point, the loop terminates.

The final value of zeros is returned as the number of trailing zeros in n!.

Notes:

Time complexity: O(log n), where n is the input integer. The loop executes log base 5 of n times.

Space complexity: O(1), as the algorithm only uses a constant amount of additional memory to store the zeros variable.
"""

# Test 1: n == 0
n = 0
trailing_zeroes = Solution().trailingZeroes(n)
expected = 0
assert trailing_zeroes == expected, f"Expected {expected} but got {trailing_zeroes}"

# Test 2: n == single digit
n = 5
trailing_zeroes = Solution().trailingZeroes(n)
expected = 1
assert trailing_zeroes == expected, f"Expected {expected} but got {trailing_zeroes}"

# Test 3: n == double digits
n = 25
trailing_zeroes = Solution().trailingZeroes(n)
expected = 6
assert trailing_zeroes == expected, f"Expected {expected} but got {trailing_zeroes}"

# Test 4: n == max input
n = 10**4
trailing_zeroes = Solution().trailingZeroes(n)
expected = 2499
assert trailing_zeroes == expected, f"Expected {expected} but got {trailing_zeroes}"
