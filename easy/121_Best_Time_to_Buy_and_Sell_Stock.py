from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price, max_profit = float('inf'), 0

        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)

        return max_profit


"""
Explanation:

Initialize min_price to infinity and max_profit to 0. Then iterate through the array of prices. For each price in the array, check if the current price < the min_price. If it is, update the min_price to the current price. Then, calculate the potential profit that could be made if the stock were to be sold at the current price by subtracting the min_price from the current price. Then checks if this potential profit > the current max_profit. If it is, it update the max_profit to the new potential profit.

After iterating through all the prices in the array, return the max_profit.

Notes:

Time Complexity: O(n), where n is the length of the prices array, as we iterate through the array once.

Space Complexity: O(1), as we only use two variables, min_price and max_profit, regardless of the size of the prices array.
"""

# Test 1: Single price
prices = [1]
max_profit = Solution().maxProfit(prices)
expected = 0
assert max_profit == expected, f"Expected {expected} but got {max_profit}"

# Test 2: Increasing price
prices = [1, 5, 7, 12]
max_profit = Solution().maxProfit(prices)
expected = prices[-1] - prices[0]
assert max_profit == expected, f"Expected {expected} but got {max_profit}"

# Test 3: Decreasing price
prices = [12, 7, 5, 1]
max_profit = Solution().maxProfit(prices)
expected = 0
assert max_profit == expected, f"Expected {expected} but got {max_profit}"

# Test 4: All same price
prices = [5, 5, 5, 5]
max_profit = Solution().maxProfit(prices)
expected = 0
assert max_profit == expected, f"Expected {expected} but got {max_profit}"

# Test 5: Peak / trough pattern
prices = [7, 2, 5, 1, 8]
max_profit = Solution().maxProfit(prices)
expected = 7
assert max_profit == expected, f"Expected {expected} but got {max_profit}"

# Test 6: Peak / through w/ zeroes
prices = [7, 2, 5, 0, 1, 8]
max_profit = Solution().maxProfit(prices)
expected = 8
assert max_profit == expected, f"Expected {expected} but got {max_profit}"
