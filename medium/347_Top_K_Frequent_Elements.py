import heapq
from collections import Counter
from typing import List

class Solution:
  def topKFrequent(self, nums, k) -> List[int]:
    heap = []
    frequency = Counter(nums)
    freq_list = [(val, key) for key, val in frequency.items()]

    for freq in freq_list:
      if len(heap) < k:
        heapq.heappush(heap, freq)
      else:
        if freq > heap[0]:
          heapq.heappop(heap)
          heapq.heappush(heap, freq)

    return [val for freq, val in heap]

"""
Explanation:

Create a heap to store the most frequent elements. Count the frequency of each element in the list using the Counter method. Create a list of tuples with the frequency as the first element and the value as the second element. Iterate over the frequency list. If the heap is not full, push the current frequency-value tuple onto the heap. If the heap is full, pop the smallest frequency-value tuple from the heap and push the current frequency-value tuple onto the heap if the current frequency is larger than the smallest frequency in the heap. Return the values of the k most frequent elements in the list.

Notes:

Time Complexity: O(n log k), where n is the length of the input array nums. The time complexity is dominated by the use of the min-heap, which has a time complexity of O(n log k) for inserting k elements.

Space Complexity: O(n), where n is the length of the input array nums. The frequency hash map and the min-heap both require O(n) space to store.
"""

# Test 1: Single element
nums = [1]
k = 1
result = Solution().topKFrequent(nums, k)
assert result == [1], f"Expected [1] but got {result}"

# Test 2: Multiple elements, multiple frequencies
nums = [1, 1, 2, 2, 2, 3, 4, 4, 4, 4, 5]
k = 3
result = Solution().topKFrequent(nums, k)
assert result == [1, 2, 4], f"Expected [1, 2, 4] but got {result}"

# Test 3: k equal to number of unique elements
nums = [1, 1, 2, 2, 2, 3, 3, 4, 4, 5]
k = 5
result = Solution().topKFrequent(nums, k)
assert result == [5, 1, 3, 2, 4], f"Expected [5, 1, 3, 2, 4] but got {result}"