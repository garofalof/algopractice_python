import heapq
from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = [(matrix[r][0], r, 0) for r in range(min(k, len(matrix)))]
        heapq.heapify(heap)

        while k:
            node, r, c = heapq.heappop(heap)

            if c < len(matrix) - 1:
                heapq.heappush(heap, (matrix[r][c + 1], r, c + 1))

            k -= 1

        return node


"""
Explanation:

Create a min-heap with the first element from each row of the matrix. Then repeatedly pop the smallest element from the heap and push the next element from the same row into the heap until we have popped k elements. The kth element we pop will be the kth smallest element in the matrix.

Notes:

Time complexity: O(x + k log x), where x is equal to min(k, length of matrix). It takes x time to construct and heapify the heap. We then perform log x insertions into the heap k times.

Space complexity: O(x), where x is equal to min(k, length of matrix).
"""

# Test 1: Single element, k == 1
matrix = [[1]]
k = 1
k_smallest = Solution().kthSmallest(matrix, k)
expected = 1
assert k_smallest == expected, f"Expected {expected} but got {k_smallest}"

# Test 2: Large matrix, k == smallest element
matrix = [[1, 3, 5, 9], [4, 7, 9, 12], [8, 14, 19, 23], [17, 21, 32, 45]]
k = 1
k_smallest = Solution().kthSmallest(matrix, k)
expected = 1
assert k_smallest == expected, f"Expected {expected} but got {k_smallest}"

# Test 3: Large matrix, k == largest element
matrix = [[1, 3, 5, 9], [4, 7, 9, 12], [8, 14, 19, 23], [17, 21, 32, 45]]
k = len(matrix) ** 2
k_smallest = Solution().kthSmallest(matrix, k)
expected = 45
assert k_smallest == expected, f"Expected {expected} but got {k_smallest}"

# Test 4: Large matrix, k == random
matrix = [[1, 3, 5, 9], [4, 7, 9, 12], [8, 14, 19, 23], [17, 21, 32, 45]]
k = 7
k_smallest = Solution().kthSmallest(matrix, k)
expected = 9
assert k_smallest == expected, f"Expected {expected} but got {k_smallest}"

# Test 5: Duplicates
matrix = [[1, 2], [2, 3]]
k = 2
k_smallest = Solution().kthSmallest(matrix, k)
expected = 2
assert k_smallest == expected, f"Expected {expected} but got {k_smallest}"
