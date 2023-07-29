import heapq


class MedianFinder:
    def __init__(self):
        self.max_heap = []
        self.min_heap = []

    def addNum(self, num):
        if not self.min_heap:
            heapq.heappush(self.min_heap, num)
            return

        if len(self.max_heap) == len(self.min_heap):
            if num < -self.max_heap[0]:
                heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
                heapq.heappush(self.max_heap, -num)
            else:
                heapq.heappush(self.min_heap, num)
        else:
            if num > self.min_heap[0]:
                heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))
                heapq.heappush(self.min_heap, num)
            else:
                heapq.heappush(self.max_heap, -num)

    def findMedian(self):
        low_size = len(self.max_heap)
        high_size = len(self.min_heap)

        if low_size == 0 and high_size == 0:
            return None

        if low_size == high_size:
            return (-self.max_heap[0] + self.min_heap[0]) / 2

        return self.min_heap[0]

"""
Explanation:

Initialize max and min heaps. The max heap will be used to store the smaller values, and the min heap will be used to store the larger values.

For the addNum method: if min heap is empty, add the num to min heap and exit. Else check to see if max heap and min heap are of same size. If so, check to see if num < max heap top. If so, add the popped top to the min heap and insert the num into the max heap. Else push the num to the min heap. If the two heaps aren't of same size, check to see if the num > min heap top. If so, push the popped min heap top to the max heap and add the num to min heap. Else add the num to the max heap.

For findMedian: if both heaps are empty, return null. Else check to see if they're the same size. If so, get average of the tops and return that value. Else return the min heap top.

Notes:

Time complexity: O(log n) for addNum, O(1) for findMedian

Space complexity: O(n) for storing the heaps
"""

# Test Case 1: Test add num
mf = MedianFinder()
mf.addNum(5)
result = mf.findMedian()
expected = 5
assert result == expected, f"Expected {expected} but got {result}"

# Test Case 2: Test empty
mf = MedianFinder()
result = mf.findMedian()
expected = None
assert result == expected, f"Expected {expected} but got {result}"

# Test Case 3: Test add ascending
mf = MedianFinder()
mf.addNum(1)
mf.addNum(3)
mf.addNum(5)
mf.addNum(7)
result = mf.findMedian()
expected = 4
assert result == expected, f"Expected {expected} but got {result}"

# Test Case 4: Test add descending
mf = MedianFinder()
mf.addNum(7)
mf.addNum(5)
mf.addNum(3)
mf.addNum(1)
result = mf.findMedian()
expected = 4
assert result == expected, f"Expected {expected} but got {result}"

# Test Case 5: Test repeating
mf = MedianFinder()
mf.addNum(1)
mf.addNum(1)
mf.addNum(1)
mf.addNum(1)
result = mf.findMedian()
expected = 1
assert result == expected, f"Expected {expected} but got {result}"

# Test Case 6: Test random operations
mf = MedianFinder()
mf.addNum(1)
mf.addNum(5)
result = mf.findMedian()
expected = 3
assert result == expected, f"Expected {expected} but got {result}"
mf.addNum(-3)
mf.addNum(4)
result = mf.findMedian()
expected = 2.5
assert result == expected, f"Expected {expected} but got {result}"
