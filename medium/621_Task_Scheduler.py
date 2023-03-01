from collections import Counter
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freqs = Counter(tasks)
        max_freq = max(freqs.values())
        max_freq_count = sum(1 for freq in freqs.values() if freq == max_freq)
        intervals = (max_freq - 1) * (n + 1) + max_freq_count

        return max(len(tasks), intervals)


"""
Explanation:

Initialize a Counter dictionary to count the frequency of each task in the input list 'tasks'. Get the maximum frequency of any task in the dictionary and the count of tasks with this frequency.

The least interval required is either equal to the length of 'tasks' list or the maximum idle time between two tasks. The maximum idle time between two tasks can be calculated by first subtracting 1 from the maximum frequency and multiplying the result with (n+1), where 'n' is the given cooldown period. The +1 is added to account for the last execution of the task. We add the number of tasks with maximum frequency to this value, as we can fill up these spots with the task with the maximum frequency. Return the maximum of these two values as the result.

Notes:

Time Complexity: O(n), where n is the length of the 'tasks' list, as we count the frequency of each task.

Space Complexity: O(1), as our dictionary is of fixed size 26.
"""

# Test 1: Min input values
tasks = ['A']
n = 0
least_interval = Solution().leastInterval(tasks, n)
expected = 1
assert least_interval == expected, f"Expected {expected} but got {least_interval}"

# Test 2: n == 0, multiples tasks
tasks = ['A', 'B', 'C']
n = 0
least_interval = Solution().leastInterval(tasks, n)
expected = 3
assert least_interval == expected, f"Expected {expected} but got {least_interval}"

# Test 3: n == 1, one task repeated
tasks = ['A', 'A', 'A', 'B', 'C']
n = 1
least_interval = Solution().leastInterval(tasks, n)
expected = 5
assert least_interval == expected, f"Expected {expected} but got {least_interval}"

# Test 4: n > length of tasks
tasks = ['A', 'B', 'C']
n = 4
least_interval = Solution().leastInterval(tasks, n)
expected = 3
assert least_interval == expected, f"Expected {expected} but got {least_interval}"

# Test 5: Multiple tasks, no idle time
tasks = ['A', 'A', 'B', 'B', 'C', 'C']
n = 1
least_interval = Solution().leastInterval(tasks, n)
expected = 6
assert least_interval == expected, f"Expected {expected} but got {least_interval}"

# Test 6: Multiple tasks, some idle time
tasks = ['A', 'A', 'A', 'A', 'B', 'B', 'C', 'C']
n = 2
least_interval = Solution().leastInterval(tasks, n)
expected = 10
assert least_interval == expected, f"Expected {expected} but got {least_interval}"
