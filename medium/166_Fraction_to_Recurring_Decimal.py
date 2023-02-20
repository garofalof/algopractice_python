class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if not numerator:
            return '0'

        sign = '-' if numerator * denominator < 0 else ''
        num, den = abs(numerator), abs(denominator)
        result = sign + str(num // den)
        remainder = num % den

        if not remainder:
            return result

        result += '.'
        map = {}

        while remainder:
            map[remainder] = len(result)

            remainder *= 10
            result += str(remainder // den)
            remainder %= den

            if remainder in map:
                index = map[remainder]

                return f"{result[:index]}({result[index:]})"

        return result


"""
Explanation:

Check if the numerator is 0, if so, return "0". Determine the sign of the result based on the signs of the numerator and denominator. Compute the absolute values of the numerator and denominator. Compute the integer part of the result by dividing the numerator by the denominator using integer division. Append the integer part to the result. Compute the remainder after the division. If there is no remainder, return the result. Append a decimal point to the result. While there is a non-zero remainder, multiply the remainder by 10, divide by the denominator, and append the quotient to the result. If the remainder is already in the map, the decimal is repeating. Return the result with the repeating portion enclosed in parentheses. Otherwise, add the remainder to the map and continue the loop. Once done, return the result.

Notes:

Time complexity: O(n), where n is the length of the repeating decimal if there is one, or the number of decimal digits otherwise.

Space complexity: O(n), where n is the length of the repeating decimal if there is one, or the number of decimal digits otherwise.
"""

# Test 1: Numerator is 0
numerator = 0
denominator = 1
result = Solution().fractionToDecimal(numerator, denominator)
expected = '0'
assert result == expected, f"Expected {expected} but got {result}"

# Test 2: Min numerator, denominator 1
numerator = -2 ** 31
denominator = 1
result = Solution().fractionToDecimal(numerator, denominator)
expected = f"{-2 ** 31}"
assert result == expected, f"Expected {expected} but got {result}"

# Test 3: Max numerator, denominator 1
numerator = 2 ** 31 - 1
denominator = 1
result = Solution().fractionToDecimal(numerator, denominator)
expected = f"{2 ** 31 - 1}"
assert result == expected, f"Expected {expected} but got {result}"

# Test 4: Min denominator, numerator 1
numerator = 1
denominator = -2 ** 31
result = Solution().fractionToDecimal(numerator, denominator)
expected = "-0.0000000004656612873077392578125"
assert result == expected, f"Expected {expected} but got {result}"

# Test 5: Max denominator, numerator 1
numerator = 1
denominator = 2 ** 31
result = Solution().fractionToDecimal(numerator, denominator)
expected = "0.0000000004656612873077392578125"
assert result == expected, f"Expected {expected} but got {result}"

# Test 6: No remainder, both positive
numerator = 2
denominator = 1
result = Solution().fractionToDecimal(numerator, denominator)
expected = "2"
assert result == expected, f"Expected {expected} but got {result}"

# Test 7: No remainder, both negative
numerator = -2
denominator = -1
result = Solution().fractionToDecimal(numerator, denominator)
expected = "2"
assert result == expected, f"Expected {expected} but got {result}"

# Test 8: No remainder, mixed
numerator = -2
denominator = 1
result = Solution().fractionToDecimal(numerator, denominator)
expected = "-2"
assert result == expected, f"Expected {expected} but got {result}"

# Test 9: Remainder, both positive, not repeating
numerator = 1
denominator = 2
result = Solution().fractionToDecimal(numerator, denominator)
expected = "0.5"
assert result == expected, f"Expected {expected} but got {result}"

# Test 10: Remainder, both negative, not repeating
numerator = -1
denominator = -2
result = Solution().fractionToDecimal(numerator, denominator)
expected = "0.5"
assert result == expected, f"Expected {expected} but got {result}"

# Test 11: Remainder, mixed, not repeating
numerator = -1
denominator = 2
result = Solution().fractionToDecimal(numerator, denominator)
expected = "-0.5"
assert result == expected, f"Expected {expected} but got {result}"

# Test 9: Remainder, both positive, repeating
numerator = 1
denominator = 3
result = Solution().fractionToDecimal(numerator, denominator)
expected = "0.(3)"
assert result == expected, f"Expected {expected} but got {result}"

# Test 10: Remainder, both negative, repeating
numerator = -1
denominator = -3
result = Solution().fractionToDecimal(numerator, denominator)
expected = "0.(3)"
assert result == expected, f"Expected {expected} but got {result}"

# Test 11: Remainder, mixed, not repeating
numerator = -1
denominator = 3
result = Solution().fractionToDecimal(numerator, denominator)
expected = "-0.(3)"
assert result == expected, f"Expected {expected} but got {result}"
