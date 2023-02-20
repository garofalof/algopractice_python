class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0

        for i in range(32):
            result *= 2
            result += n & 1
            n //= 2

        return result


"""
Explanation:

Initialize the result variable to 0 and then loop 32 times using a for loop. For each iteration of the loop, shift result left by one bit and set the least significant bit of result to the current least significant bit of n. Then divide n by 2 using integer division to shift its bits right by one position. Finally, return the result.

Notes:

Time Complexity: O(1), since we loop exactly 32 times, which is a constant number of iterations.

Space Complexity: O(1), since we only use a constant amount of space to store result.
"""

# Test 1: Value of 0
num = 0
reversed_bits = Solution().reverseBits(num)
expected = 0
assert reversed_bits == expected, f"Expected {expected} but got {reversed_bits}"

# Test 2: Value of 1
num = 1
reversed_bits = Solution().reverseBits(num)
expected = 2 ** 31
assert reversed_bits == expected, f"Expected {expected} but got {reversed_bits}"

# Test 3: Max value
num = 2 ** 31 - 1
reversed_bits = Solution().reverseBits(num)
expected = 4294967294
assert reversed_bits == expected, f"Expected {expected} but got {reversed_bits}"
