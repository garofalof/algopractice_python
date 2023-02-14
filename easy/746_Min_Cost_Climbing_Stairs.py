from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)

        for i in reversed(range(0, len(cost) - 3)):
            cost[i] += min(cost[i + 1], cost[i + 2])

        return min(cost[0], cost[1])


"""
Explanation:

Add 0 to the end of the cost list to represent the cost of reaching the top of the staircase. Starting from the second to last step and moving backward, for each step i, find the minimum cost between reaching that step from the next step or two steps ahead and add it to the cost of reaching that step. Return the minimum cost of reaching either the first or second step.

Notes:

Time complexity: O(n)

Space complexity: O(1)
"""

# Test 1: Min length of 2
cost_list = [0, 1]
cost = Solution().minCostClimbingStairs(cost_list)
expected = min(cost_list[0], cost_list[1])
assert cost == expected, f"Expected {expected} but got {cost}"

# Test 2: All elements min value of 0
cost_list = [0, 0, 0, 0]
cost = Solution().minCostClimbingStairs(cost_list)
expected = 0
assert cost == expected, f"Expected {expected} but got {cost}"

# Test 3: All elements max value of 999
cost_list = [999, 999, 999, 999]
cost = Solution().minCostClimbingStairs(cost_list)
expected = 1998
assert cost == expected, f"Expected {expected} but got {cost}"

# Test 4: All elements increasing
cost_list = [1, 2, 3, 4]
cost = Solution().minCostClimbingStairs(cost_list)
expected = 4
assert cost == expected, f"Expected {expected} but got {cost}"

# Test 5: All elements decreasing
cost_list = [4, 3, 2, 1]
cost = Solution().minCostClimbingStairs(cost_list)
expected = 4
assert cost == expected, f"Expected {expected} but got {cost}"

# Test 6: Mixed values
cost_list = [1, 100, 5, 75, 10]
cost = Solution().minCostClimbingStairs(cost_list)
expected = 16
assert cost == expected, f"Expected {expected} but got {cost}"
