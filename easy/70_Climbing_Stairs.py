class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1

        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]

"""
Explanation:

Build an array `dp` where each index represents the number of stairs, and the value at that index represents the number of distinct ways to reach that number of stairs. The base cases are initialized as dp[1] = 1 and dp[2] = 2 since there is only one way to climb 1 stair and two ways to climb 2 stairs. Then, starting from the third stair, the code iteratively fills in the dp array using the recurrence relation dp[i] = dp[i - 1] + dp[i - 2]. This means that the number of distinct ways to climb i stairs is equal to the sum of the number of ways to climb i - 1 stairs and the number of ways to climb i - 2 stairs. Finally, the code returns dp[n], which represents the number of distinct ways to climb n stairs.

Notes:

Time complexity: O(n)

Space complexity: O(n)
"""

# Test Case 1: n == 1
n = 1
result = Solution().climbStairs(n)
expected = 1
assert result == expected, f"Expected {expected} but got {result}"

# Test Case 2: n == 2
n = 2
result = Solution().climbStairs(n)
expected = 2
assert result == expected, f"Expected {expected} but got {result}"

# Test Case 3: n is odd
n = 5
result = Solution().climbStairs(n)
expected = 8
assert result == expected, f"Expected {expected} but got {result}"

# Test Case 4: n is even
n = 8
result = Solution().climbStairs(n)
expected = 34
assert result == expected, f"Expected {expected} but got {result}"

# Test Case 5: n == max value
n = 45
result = Solution().climbStairs(n)
expected = 1836311903
assert result == expected, f"Expected {expected} but got {result}"