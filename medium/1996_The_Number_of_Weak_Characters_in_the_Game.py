from typing import List


class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key=lambda x: (-x[0], x[1]))
        result, defense_max = 0, 0

        for _, defense in properties:
            if defense < defense_max:
                result += 1

            defense_max = max(defense_max, defense)

        return result


"""
Explanation:

Sort the list by descending order of attack, and for those with equal attack, ascending order of defense. Initialize the result and defense_max variables to 0, and iterate through each character in the sorted list. If the defense of the current character < defense_max, it means that there exists at least one other character with higher defense and equal or higher attack. Thus, we increment the result by 1. At each iteration, update defense_max with the maximum of the current defense and defense_max. Once done, the final value of result is returned as the number of weak characters.

Notes:

Time complexity: O(n log n) due to the sorting step, where n is the length of the input list.

Space complexity: O(log n), as we use extra space for sorting the list.
"""

# Test 1: No weak characters
characters = [[1, 3], [2, 2], [3, 1]]
num_weak = Solution().numberOfWeakCharacters(characters)
expected = 0
assert num_weak == expected, f"Expected {expected} but got {num_weak}"

# Test 2: Different attack, all weak
characters = [[1, 1], [2, 2], [3, 3]]
num_weak = Solution().numberOfWeakCharacters(characters)
expected = 2
assert num_weak == expected, f"Expected {expected} but got {num_weak}"

# Test 3: Different attack, some weak
characters = [[1, 3], [2, 1], [3, 2]]
num_weak = Solution().numberOfWeakCharacters(characters)
expected = 1
assert num_weak == expected, f"Expected {expected} but got {num_weak}"

# Test 4: Same attack, none weak
characters = [[1, 1], [2, 2], [3, 3], [3, 3]]
num_weak = Solution().numberOfWeakCharacters(characters)
expected = 2
assert num_weak == expected, f"Expected {expected} but got {num_weak}"

# Test 5: Same attack, weak
characters = [[1, 1], [2, 2], [2, 1], [3, 3]]
num_weak = Solution().numberOfWeakCharacters(characters)
expected = 3
assert num_weak == expected, f"Expected {expected} but got {num_weak}"
