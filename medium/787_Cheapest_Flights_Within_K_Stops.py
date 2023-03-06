from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float('inf')] * n
        prices[src] = 0

        for _ in range(k + 1):
            temp = prices[:]

            for source, dest, price in flights:
                if temp[dest] > prices[source] + price:
                    temp[dest] = prices[source] + price

            prices = temp

        return -1 if prices[dst] == float('inf') else prices[dst]


"""
Explanation:

Initialize the prices list with infinity values and set the source node price to 0. This step is necessary to keep track of the minimum price to reach each node from the source node.
Update the prices list iteratively up to k + 1 stops, as the maximum number of stops allowed to reach the destination is k + 1. In each iteration, we create a new temp list and update it according to the minimum price to reach each node from the source node up to i stops.
In the inner loop, we iterate through each flight and update the price of the destination node if it can be reached at a cheaper price from the current source node.

Once done, return -1 if the destination node is unreachable (i.e. its price is still infinity), else return the final price of the destination node.

Notes:

Time complexity: O(k * m), where k is the number of stops allowed and m is the length of the flights list.

Space complexity: O(n), where n is the number of nodes in the graph, as we create a prices list of length n to store the cheapest prices from the source to each node in the graph.
"""

# Test 1: No flight from src to dst
n = 3
flights = [[0, 2, 100], [1, 0, 100], [2, 0, 500]]
src = 0
dst = 1
k = 1
cheapest = Solution().findCheapestPrice(n, flights, src, dst, k)
expected = -1
assert cheapest == expected, f"Expected {expected} but got {cheapest}"

# Test 2: No flights
n = 3
flights = []
src = 0
dst = 1
k = 1
cheapest = Solution().findCheapestPrice(n, flights, src, dst, k)
expected = -1
assert cheapest == expected, f"Expected {expected} but got {cheapest}"

# Test 3: One flight from src to dst
n = 3
flights = [[0, 1, 500], [0, 2, 100], [2, 0, 100]]
src = 0
dst = 1
k = 1
cheapest = Solution().findCheapestPrice(n, flights, src, dst, k)
expected = 500
assert cheapest == expected, f"Expected {expected} but got {cheapest}"

# Test 4: Multiple flights from src to dst
n = 3
flights = [[0, 1, 500], [0, 2, 100], [2, 1, 100]]
src = 0
dst = 1
k = 1
cheapest = Solution().findCheapestPrice(n, flights, src, dst, k)
expected = 200
assert cheapest == expected, f"Expected {expected} but got {cheapest}"

# Test 5: Can't reach dst from src in k stops
n = 4
flights = [[0, 1, 200], [1, 3, 100], [3, 2, 200], [2, 1, 400]]
src = 0
dst = 2
k = 1
cheapest = Solution().findCheapestPrice(n, flights, src, dst, k)
expected = -1
assert cheapest == expected, f"Expected {expected} but got {cheapest}"
