from typing import List


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    def employeeFreeTime(self, schedule: List[List[int]]) -> List[Interval]:
        schedules = []

        for emp in schedule:
            for i in range(0, len(emp), 2):
                start, end = emp[i], emp[i + 1]
                schedules.append(Interval(start, end))

        schedules.sort(key=lambda x: x.start)
        result = []

        prev_end = schedules[0].end

        for interval in schedules[1:]:
            if interval.start > prev_end:
                result.append(Interval(prev_end, interval.start))
            prev_end = max(prev_end, interval.end)

        return result


"""
Explanation:

The code initializes an empty list schedules to store individual intervals. It iterates over each employee's schedule and extracts pairs of start and end times, creating Interval objects for each pair. These intervals are added to the schedules list. The schedules list is sorted based on the start times of the intervals. The variables prev, start, and end are initialized with the first interval's values. The result list is initialized to store the merged intervals representing free time. The code iterates over the sorted schedules list, starting from the second interval. For each interval, it checks if the current interval's start time is greater than or equal to the previous interval's end time. If so, it means there is a gap between the intervals, and a new free time interval is created and added to the result list. The start variable is updated to the current interval's start time. The end variable is updated to the maximum of the current interval's end time and the previous interval's end time. Finally, the result list containing the merged intervals representing free time is returned.

Notes:

Time complexity: O(n log n), as we sort the input list

Space complexity: O(n) to store schedule and result
"""

# Test Case 1: Single employee, no overlap
schedule = [[1, 2, 3, 4]]
result = [(interval.start, interval.end)
          for interval in Solution().employeeFreeTime(schedule)]
expected = [(2, 3)]
assert result == expected, f"Expected {expected} but got {result}"

# Test Case 2: Single employee, with overlap
schedule = [[1, 3, 2, 4]]
result = Solution().employeeFreeTime(schedule)
expected = []
assert result == expected, f"Expected {expected} but got {result}"

# Test Case 3: Multiple employees, no overlap
schedule = [[1, 2], [3, 4], [5, 6]]
result = [(interval.start, interval.end)
          for interval in Solution().employeeFreeTime(schedule)]
expected = [(2, 3), (4, 5)]
assert result == expected, f"Expected {expected} but got {result}"

# Test Case 4: Multiple employees, with overlap
schedule = [[1, 2, 5, 6], [1, 3], [4, 10]]
result = [(interval.start, interval.end)
          for interval in Solution().employeeFreeTime(schedule)]
expected = [(3, 4)]
assert result == expected, f"Expected {expected} but got {result}"

# Test Case 5: Single employee, all-day schedule
schedule = [[0, 24]]
result = Solution().employeeFreeTime(schedule)
expected = []
assert result == expected, f"Expected {expected} but got {result}"

# Test Case 6: Multiple employees, all-day schedule
schedule = [[0, 24], [5, 6, 7, 8], [1, 3, 4, 5]]
result = Solution().employeeFreeTime(schedule)
expected = []
assert result == expected, f"Expected {expected} but got {result}"