class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0

        is_prime = [True] * n
        is_prime[0], is_prime[1] = False, False

        for i in range(2, int(n ** 0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, n, i):
                    is_prime[j] = False

        return sum(is_prime)


"""
Explanation:

Start by creating an array of boolean values, where each value represents whether the index is a prime number or not. Initially, all values are set to True, except for the first two values, which are set to False because 1 is not prime and 0 is not a positive integer. Loop through all values <= to the square root of n. For each value, if it's prime, all its multiples are set to False because they aren't prime. Return the number of primes by summing up all True values in the array.

Notes:

Time complexity: O(n * log(log(n))), as the outer loop runs n times, and the inner loop runs log(n) times for each value in the outer loop, so the time complexity is O(n * log(n)). However, because the inner loop starts from i * i, the actual running time is reduced to O(n * log(log(n))).

Space complexity: O(n)
"""

# Test 1: n = 0
result = Solution().countPrimes(0)
assert result == 0, f"Expected 0 but got {result}"

# Test 2: n = 1
result = Solution().countPrimes(1)
assert result == 0, f"Expected 0 but got {result}"

# Test 3: n = 2
result = Solution().countPrimes(2)
assert result == 0, f"Expected 0 but got {result}"

# Test 4: n = 3
result = Solution().countPrimes(3)
assert result == 1, f"Expected 1 but got {result}"

# Test 5: n = 10
result = Solution().countPrimes(10)
assert result == 4, f"Expected 4 but got {result}"
