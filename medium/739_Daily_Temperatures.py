from typing import List


class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        result = [0] * len(temps)
        stack = []

        for i, temp in enumerate(temps):
            while stack and temps[stack[-1]] < temp:
                prev = stack.pop()
                result[prev] = i - prev

            stack.append(i)

        return result


"""
Explanation:

Initialize a result array of all 0's with length equal to the input temps array to hold the number of days to wait until a warmer temperature. Also initialize an empty stack to hold indices of temperatures we have not yet found a warmer day for.

Loop through each temperature in the input temps array and for each temperature, check if there are any previous temperatures in the stack that are cooler than the current temperature. If there are, pop those indices from the stack and calculate the number of days to wait until a warmer temperature using the current index minus the popped index. Then set the result at the popped index to this number of days. Keep popping until there are no more previous temperatures in the stack that are cooler than the current temperature.

Finally, append the current temperature's index to the stack since we have not yet found a warmer day for it. After looping through all the temperatures, return the result array containing the number of days to wait until a warmer temperature for each temperature in the input temps array.

Notes:

Time complexity: O(n), where n is the length of the input temps array, since each temperature is processed only once and the stack operations take constant time.

Space complexity: O(n), as we use extra space of size n for the result array and the stack.
"""

# Test 1: Single temp
temps = [10]
daily_temps = Solution().dailyTemperatures(temps)
expected = [0]
assert daily_temps == expected, f"Expected {expected} but got {daily_temps}"

# Test 2: Same temps
temps = [30, 30, 30, 30]
daily_temps = Solution().dailyTemperatures(temps)
expected = [0, 0, 0, 0]
assert daily_temps == expected, f"Expected {expected} but got {daily_temps}"

# Test 3: Increasing temps
temps = [10, 20, 30, 40]
daily_temps = Solution().dailyTemperatures(temps)
expected = [1, 1, 1, 0]
assert daily_temps == expected, f"Expected {expected} but got {daily_temps}"

# Test 4: Decreasing temps
temps = [40, 30, 20, 10]
daily_temps = Solution().dailyTemperatures(temps)
expected = [0, 0, 0, 0]
assert daily_temps == expected, f"Expected {expected} but got {daily_temps}"

# Test 5: Sawtooth pattern
temps = [10, 50, 30, 60, 20, 70]
daily_temps = Solution().dailyTemperatures(temps)
expected = [1, 2, 1, 2, 1, 0]
assert daily_temps == expected, f"Expected {expected} but got {daily_temps}"

# Test 6: All same except one
temps = [30, 30, 40, 30]
daily_temps = Solution().dailyTemperatures(temps)
expected = [2, 1, 0, 0]
assert daily_temps == expected, f"Expected {expected} but got {daily_temps}"
