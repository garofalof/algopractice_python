from typing import List


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        times = sorted([int(time[:2]) * 60 + int(time[3:])
                       for time in timePoints])
        min_diff = min(times[i+1] - times[i] for i in range(len(times)-1))
        circular_diff = 1440 - (times[-1] - times[0]) if len(times) > 1 else 0

        return min(min_diff, circular_diff)


"""
Explanation:

First, convert each time string in the timePoints list to an integer representing the total number of minutes since midnight and sort these times in ascending order. Then, compute the minimum difference between consecutive times.

If there's at least two times in the list, compute the circular difference (i.e., the difference between the last time and the first time, accounting for the fact that the times wrap around at midnight) and return the minimum of the circular difference or mininimum difference.

Notes:

Time complexity: O(n log n), where n is the length of the timePoints list, as we need to sort the input list.

Space complexity: O(n), where n is the length of the input list. This is due to the use of the times list to store the converted times.
"""

# Test 1: Two times, not circular
times = ['01:22', '02:33']
min_difference = Solution().findMinDifference(times)
expected = 71
assert min_difference == expected, f"Expected {expected} but got {min_difference}"

# Test 2: Two times, circular
times = ['23:59', '00:01']
min_difference = Solution().findMinDifference(times)
expected = 2
assert min_difference == expected, f"Expected {expected} but got {min_difference}"

# Test 3: Two times, same
times = ['23:59', '23:59']
min_difference = Solution().findMinDifference(times)
expected = 0
assert min_difference == expected, f"Expected {expected} but got {min_difference}"

# Test 4: > two times, not circular
times = ['01:22', '03:11', '04:35', '05:49', '06:00']
min_difference = Solution().findMinDifference(times)
expected = 11
assert min_difference == expected, f"Expected {expected} but got {min_difference}"

# Test 5: > two times, circular
times = ['03:11', '04:35', '05:49', '23:59', '00:01']
min_difference = Solution().findMinDifference(times)
expected = 2
assert min_difference == expected, f"Expected {expected} but got {min_difference}"
