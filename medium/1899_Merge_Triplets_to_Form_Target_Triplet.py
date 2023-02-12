from typing import List


class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        first, second, third = False, False, False
        t1, t2, t3 = target

        for a, b, c in triplets:
            if a == t1 and b <= t2 and c <= t3:
                first = True
            if b == t2 and a <= t1 and c <= t3:
                second = True
            if c == t3 and a <= t1 and b <= t2:
                third = True
            if all([first, second, third]):
                return True

        return False


"""
Explanation:

Use three variables first, second, and third to track if a match has been found for each element of target. For each triplet, use three if statements to compare the elements of the triplet with the elements of target. For each element, if the element is equal to its target and the other elements are <= their targets, mark the found match as True. If all three matches are found, return True. If no match is found, return False.

Notes:

Time Complexity: O(n)
Space Complexity: O(1)
"""

# Test 1: Regular case
triplets = [[2, 1, 3], [1, 7, 3], [2, 4, 5]]
target = [2, 7, 5]
can_merge = Solution().mergeTriplets(triplets, target)
assert can_merge == True, f"Expected True but got {can_merge}"

# Test 2: No matching triplets
triplets = [[1, 2, 3], [3, 2, 1], [1, 3, 2]]
target = [2, 3, 1]
can_merge = Solution().mergeTriplets(triplets, target)
assert can_merge == False, f"Expected False but got {can_merge}"

# Test 3: Single triplet match
triplets = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
target = [1, 2, 3]
can_merge = Solution().mergeTriplets(triplets, target)
assert can_merge == True, f"Expected True but got {can_merge}"

# Test 4: All values match
triplets = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
target = [1, 1, 1]
can_merge = Solution().mergeTriplets(triplets, target)
assert can_merge == True, f"Expected True but got {can_merge}"
