class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0

        while n != 0:
            count += 1
            n = n & (n - 1)

        return count

"""
Explanation:

Use a while loop to keep checking n until it's 0. For each iteration, increment the count by 1 and perform a bitwise AND operation between n and n-1, which sets the rightmost 1 bit in n to 0. Continue until all 1 bits in n have been set to 0 and the while loop terminates. Return the final count as the hamming weight of the given integer.

Notes:

Time Complexity: O(1), as n is constrained as a 32-bit integer.
Space Complexity: O(1), as the code only uses a single integer variable to keep track of the count.
"""

# Test 1: No significant bits
n = 0
weight = Solution().hammingWeight(n)
assert weight == 0, f"Expected 0 but got {weight}"

# Test 2: Single significant bit
n = 1
weight = Solution().hammingWeight(n)
assert weight == 1, f"Expected 1 but got {weight}"

# Test 3: Multiple significant bits
n = 7
weight = Solution().hammingWeight(n)
assert weight == 3, f"Expected 3 but got {weight}"

# Test 4: All significant bits
n = 2 ** 31 - 1
weight = Solution().hammingWeight(n)
assert weight == 31, f"Expected 31 but got {weight}"
