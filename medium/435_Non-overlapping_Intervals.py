from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda x: x[0])

        result = 0
        prev_end = intervals[0][1]

        for i in range(1, len(intervals)):
            start, end = intervals[i]

            if start >= prev_end:
                prev_end = end
            else:
                result += 1
                prev_end = min(prev_end, end)

        return result


"""
Explanation:

Sort the input intervals in ascending order of start time. Initialize a variable "result" to 0 and a variable "prev_end" to the end time of the first interval. Then iterate through the remaining intervals, checking if the start time of the current interval >= the end time of the previous interval. If it is, update "prev_end" to the end time of the current interval. If it's not, increment "result" and update "prev_end" to the minimum of the previous end time and the current end time. After iterating through all the intervals, return the final value of "result".

Notes:

Time complexity: O(n log n), where n is the number of intervals. Sorting the intervals takes O(n log n) time, and iterating through the intervals takes O(n) time.

Space complexity: O(log n) to O(n), depending on the implementation of the sorting function.
"""

# Test 1: No overlaps
intervals = [[1, 2], [3, 4], [5, 6]]
num_erased = Solution().eraseOverlapIntervals(intervals)
expected = 0
assert num_erased == expected, f"Expected {expected} but got {num_erased}"

# Test 2: Single overlap
intervals = [[1, 3], [2, 3], [4, 5]]
num_erased = Solution().eraseOverlapIntervals(intervals)
expected = 1
assert num_erased == expected, f"Expected {expected} but got {num_erased}"

# Test 3: Multiple overlaps
intervals = [[1, 3], [2, 3], [2, 4], [3, 5], [4, 6]]
num_erased = Solution().eraseOverlapIntervals(intervals)
expected = 3
assert num_erased == expected, f"Expected {expected} but got {num_erased}"

# Test 4: Single interval
intervals = [[1, 3]]
num_erased = Solution().eraseOverlapIntervals(intervals)
expected = 0
assert num_erased == expected, f"Expected {expected} but got {num_erased}"

# Test 5: All same interval
intervals = [[1, 2]] * 5
num_erased = Solution().eraseOverlapIntervals(intervals)
expected = 4
assert num_erased == expected, f"Expected {expected} but got {num_erased}"
