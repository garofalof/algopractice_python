import heapq


class Solution:
    def getKth(self, lo, hi, k):
        memo = {}

        def power(x):
            if x in memo:
                return memo[x]
            if x == 1:
                return 0

            memo[x] = 1 + power(x * 3 + 1 if x % 2 else x // 2)
            return memo[x]

        nums = [(power(i), i) for i in range(lo, hi + 1)]
        heapq.heapify(nums)

        for _ in range(k):
            result = heapq.heappop(nums)

        return result[1]

"""
Explanation:

The power function calculates the power value of a given number x based on a set of rules. It recursively calculates the power by either multiplying x by 3 and adding 1 if x is odd or dividing x by 2 if x is even. The function utilizes memoization to store and retrieve previously calculated power values. The nums list is constructed by iterating through the range from lo to hi and calculating the power value for each number. The resulting list consists of tuples containing the power value and the number itself. The heapify operation is applied to the nums, organizaing the list as a min-heap, with the smallest element at the root. In the main loop, we pop from heap k times to extract the kth smallest element from the heap. Each iteration retrieves the smallest element and updates the result.

Finally, the function returns the result, which represents the kth element in the range from lo to hi.

Notes:

Time complexity: O(n + k log n), where n is the difference between hi and lo, and k is the desired value

Space complexity: O(n) for memoization, storing nums, and recursion stack for getting power value
"""

# Test Case 1: Min range, lo == hi == k
lo = hi = k = 1
result = Solution().getKth(lo, hi, k)
expected = 1
assert result == expected, f"Expected {expected} but got {result}"

# Test Case 2: Min range, lo == hi, k == 1
lo = hi = 1000
k = 1
result = Solution().getKth(lo, hi, k)
expected = 1000
assert result == expected, f"Expected {expected} but got {result}"

# Test Case 3: Max range, max k
lo = 1
hi = 1000
k = 1000
result = Solution().getKth(lo, hi, k)
expected = 871
assert result == expected, f"Expected {expected} but got {result}"

# Test Case 4: Max range, min k
lo = 1
hi = 1000
k = 1
result = Solution().getKth(lo, hi, k)
expected = 1
assert result == expected, f"Expected {expected} but got {result}"
