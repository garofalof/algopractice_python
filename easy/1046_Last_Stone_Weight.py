import heapq
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [stone * -1 for stone in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            s1, s2 = heapq.heappop(stones), heapq.heappop(stones)

            if s1 != s2:
                heapq.heappush(stones, s1 - s2)

        return -heapq.heappop(stones) if stones else 0


"""
Explanation:

Use a heap to retrieve and remove the two heaviest stones at each iteration. First, the transform the list of stones by multiplying each element by -1, allowing us to use the min heap as a max heap. Then, transform the list into a heap.

In the while loop, repeatedly pop from the heap to retrieve the two heaviest stones (s1 and s2), which are then compared to see if they are equal. If they are not equal, the difference between the two weights is computed and added back to the heap. This process continues until there is either one stone left or no stones left.

Finally, the last stone's weight is retrieved by popping the last element from the heap, negating its value, and returning it as the result. If the heap is empty, the function returns 0.

Notes:

Time complexity: O(n log n), where n is the length of the input list stones. This is due to the cost of heapifying the list and performing n iterations of popping and pushing elements onto the heap, each of which has a log n time complexity.

Space complexity: O(n), as we are creating a new list of negated weights and a heap data structure with up to n elements.
"""

# Test 1: Single stone
stones = [1]
last_weight = Solution().lastStoneWeight(stones)
expected = 1
assert last_weight == expected, f"Expected {expected} but got {last_weight}"

# Test 2: Two stones, same weight
stones = [2, 2]
last_weight = Solution().lastStoneWeight(stones)
expected = 0
assert last_weight == expected, f"Expected {expected} but got {last_weight}"

# Test 3: Two stones, different weight
stones = [3, 5]
last_weight = Solution().lastStoneWeight(stones)
expected = 2
assert last_weight == expected, f"Expected {expected} but got {last_weight}"

# Test 4: Multiple stones, increasing
stones = [1, 3, 5, 8, 9]
last_weight = Solution().lastStoneWeight(stones)
expected = 0
assert last_weight == expected, f"Expected {expected} but got {last_weight}"

# Test 5: Multiple stones, decreasing
stones = [9, 8, 5, 3, 1]
last_weight = Solution().lastStoneWeight(stones)
expected = 0
assert last_weight == expected, f"Expected {expected} but got {last_weight}"

# Test 6: Multiple stones, mixed
stones = [2, 1, 5, 3, 7]
last_weight = Solution().lastStoneWeight(stones)
expected = 0
assert last_weight == expected, f"Expected {expected} but got {last_weight}"

# Test 7: Mutiple stones, same
stones = [5, 5, 5, 5, 5]
last_weight = Solution().lastStoneWeight(stones)
expected = 5
assert last_weight == expected, f"Expected {expected} but got {last_weight}"
