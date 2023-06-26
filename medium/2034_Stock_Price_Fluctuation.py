import heapq

class StockPrice:
    def __init__(self):
        self.data = {}
        self.maxTime = 0
        self.minHeap = []
        self.maxHeap = []

    def update(self, time, price):
        self.data[time] = price
        self.maxTime = max(self.maxTime, time)

        heapq.heappush(self.minHeap, (price, time))
        heapq.heappush(self.maxHeap, (-price, time))

    def current(self):
        return self.data[self.maxTime]

    def maximum(self):
        while self.data[self.maxHeap[0][1]] != -self.maxHeap[0][0]:
            heapq.heappop(self.maxHeap)

        return -self.maxHeap[0][0]

    def minimum(self):
        while self.data[self.minHeap[0][1]] != self.minHeap[0][0]:
            heapq.heappop(self.minHeap)

        return self.minHeap[0][0]

"""
Explanation:

Initialize the class w/ a dictionary `data` to store time / price pairs, `maxTime` to track latest timestamp, and `minHeap` and `maxHeap` to efficiently store and retrieve min and max price.  The `update` method is used to update the stock price at a given time. It adds the price to the data dictionary, keeps track of the maximum time seen so far, and adds the price-time pair to both the minHeap and maxHeap. The `current` method returns the latest recorded price, which corresponds to the maximum time. The `maximum` method retrieves the maximum price recorded so far. It pops items from the maxHeap until it finds a price that matches the corresponding time in the data dictionary. The `minimum` method retrieves the minimum price recorded so far. It follows a similar approach as the `maximum` method but uses the minHeap instead.

Notes:

Time complexity: O(log n) for `update`, `maximum`, and `minimum`, where n is the number of recorded stock prices.

Space complexity: O(n), where n is the number of recorded stock prices. The data dictionary and heaps store the price-time pairs.
"""

# Test Case 1: Basic operations
stock = StockPrice()
stock.update(1, 10)
current = stock.current()
max_price = stock.maximum()
min_price = stock.minimum()
expected_current = 10
expected_max = 10
expected_min = 10
assert current == expected_current, f"Expected {expected_current} but got {current}"
assert max_price == expected_max, f"Expected {expected_max} but got {max_price}"
assert min_price == expected_min, f"Expected {expected_min} but got {min_price}"

# Test Case 2: Normal stream
stock = StockPrice()
stock.update(1, 10)
stock.update(2, 5)
stock.update(3, 12)
stock.update(4, 7)
current = stock.current()
max_price = stock.maximum()
min_price = stock.minimum()
expected_current = 7
expected_max = 12
expected_min = 5
assert current == expected_current, f"Expected {expected_current} but got {current}"
assert max_price == expected_max, f"Expected {expected_max} but got {max_price}"
assert min_price == expected_min, f"Expected {expected_min} but got {min_price}"

# Test Case 3: Price update on max
stock = StockPrice()
stock.update(1, 10)
stock.update(2, 5)
stock.update(3, 12)
stock.update(4, 7)
stock.update(3, 4)
current = stock.current()
max_price = stock.maximum()
min_price = stock.minimum()
expected_current = 7
expected_max = 10
expected_min = 4
assert current == expected_current, f"Expected {expected_current} but got {current}"
assert max_price == expected_max, f"Expected {expected_max} but got {max_price}"
assert min_price == expected_min, f"Expected {expected_min} but got {min_price}"

# Test Case 3: Price update on min
stock = StockPrice()
stock.update(1, 10)
stock.update(2, 5)
stock.update(3, 12)
stock.update(4, 7)
stock.update(2, 20)
current = stock.current()
max_price = stock.maximum()
min_price = stock.minimum()
expected_current = 7
expected_max = 20
expected_min = 7
assert current == expected_current, f"Expected {expected_current} but got {current}"
assert max_price == expected_max, f"Expected {expected_max} but got {max_price}"
assert min_price == expected_min, f"Expected {expected_min} but got {min_price}"