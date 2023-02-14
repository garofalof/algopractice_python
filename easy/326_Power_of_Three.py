class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 1:
            return False

        while n % 3 == 0:
            n /= 3

        return n == 1


"""
Explanation:

If the input number "n" is less than 1, return False as the number cannot be a power of three. Check if a given number "n" is a power of three by dividing "n" by 3 repeatedly until "n" is no longer divisible by 3. If "n" becomes 1 after this division, then it is a power of three. If "n" becomes anything other than 1 after the division, then it is not a power of three. At the end, return the result of the check.

Notes:

Time complexity: O(log_3(n)), as the while loop divides "n" by 3 until "n" is no longer divisible by 3.

Space complexity: O(1)
"""

# Test 1: n < 1
n = 0
is_power_three = Solution().isPowerOfThree(n)
expected = False
assert is_power_three == expected, f"Expected {expected} but got {is_power_three}"

# Test 2: n == 1
n = 1
is_power_three = Solution().isPowerOfThree(n)
expected = True
assert is_power_three == expected, f"Expected {expected} but got {is_power_three}"

# Test 3: n == 3
n = 3
is_power_three = Solution().isPowerOfThree(n)
expected = True
assert is_power_three == expected, f"Expected {expected} but got {is_power_three}"

# Test 4: n power of 3 > 3
n = 27
is_power_three = Solution().isPowerOfThree(n)
expected = True
assert is_power_three == expected, f"Expected {expected} but got {is_power_three}"

# Test 5: n not power of 3
n = 36
is_power_three = Solution().isPowerOfThree(n)
expected = False
assert is_power_three == expected, f"Expected {expected} but got {is_power_three}"

# Test 6: min value
n = -2 ** 31
is_power_three = Solution().isPowerOfThree(n)
expected = False
assert is_power_three == expected, f"Expected {expected} but got {is_power_three}"

# Test 7: max value
n = 2 ** 31 - 1
is_power_three = Solution().isPowerOfThree(n)
expected = False
assert is_power_three == expected, f"Expected {expected} but got {is_power_three}"
