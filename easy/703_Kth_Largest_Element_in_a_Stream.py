import heapq
from typing import List


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = []
        self.initializeHeap(nums)

    def initializeHeap(self, nums: List[int]):
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)

        if len(self.nums) > self.k:
            heapq.heappop(self.nums)

        return self.nums[0]

"""
Explanation:

The nums list is initially stored in the self.nums attribute. The initializeHeap method is used to convert the self.nums list into a heap and ensure it contains the k largest elements. The add method adds a new value to the heap. If the length of self.nums < k, the value is pushed onto the heap. Otherwise, if the new value > the smallest value in the heap, it replaces the smallest value to maintain the k largest elements. The minimum value in the heap represents the kth largest element, so it is returned as the result.

Notes:

Time complexity: O(n log k) for initialization, and O(log k) for add operation

Space complexity: O(n) space used to store the heap
"""

# Test Case 1: Adding a value within the kth largest elements
kth_largest = KthLargest(2, [3, 5, 7, 1, 2, 9])
result = kth_largest.add(4)
expected = 7
assert result == expected, f"Expected {expected} but got {result}"

# Test Case 2: Adding a value larger than the kth largest elements
kth_largest = KthLargest(3, [9, 8, 7, 6, 5, 4, 3, 2, 1])
result = kth_largest.add(10)
expected = 8
assert result == expected, f"Expected {expected} but got {result}"

# Test Case 3: Adding a value to an empty list
kth_largest = KthLargest(1, [])
result = kth_largest.add(5)
expected = 5
assert result == expected, f"Expected {expected} but got {result}"

# Test Case 4: Adding a value to a list size k
kth_largest = KthLargest(5, [10, 20, 30, 50, 60])
result = kth_largest.add(40)
expected = 20
assert result == expected, f"Expected {expected} but got {result}"

# Test Case 5: Adding a value within the kth largest elements, maintaining order
kth_largest = KthLargest(4, [1, 3, 5, 7, 9])
result = kth_largest.add(6)
expected = 5
assert result == expected, f"Expected {expected} but got {result}"
