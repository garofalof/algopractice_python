class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        i = count = 0

        while i < len(target):
            sub = ""

            for j in range(len(source)):
                if i < len(target) and source[j] == target[i]:
                    sub += source[j]
                    i += 1

            if not sub:
                return -1

            count += 1

        return count


"""
Explanation:

Initialize the variable i and count to 0. While i < the length of the target string, loop through the source string. If the current character in the source string matches the current character in the target string, add it to the sub string and increment i. If sub is empty, return -1 since there's no way to form the target string from the source string. Otherwise, increment the count variable to keep track of how many times we looped through the source string to form the target string. Finally, return the count variable which represents the shortest way to form the target string from the source string.

Notes:

Time complexity: O(n * m), where n is the length of the target string and m is the length of the source string, as we loop through the source string for each character in the target string.

Space complexity: O(1), as we use constant extra space to hold the i, count, and sub variables.
"""

# Test 1: Same strings, length 1
src = 'a'
target = 'a'
shortest_path = Solution().shortestWay(src, target)
expected = 1
assert shortest_path == expected, f"Expected {expected} but got {shortest_path}"

# Test 2: Different strings, length 1
src = 'a'
target = 'b'
shortest_path = Solution().shortestWay(src, target)
expected = -1
assert shortest_path == expected, f"Expected {expected} but got {shortest_path}"

# Test 3: Same strings, length > 1
src = 'aabb'
target = 'aabb'
shortest_path = Solution().shortestWay(src, target)
expected = 1
assert shortest_path == expected, f"Expected {expected} but got {shortest_path}"

# Test 4: Different strings, same length > 1
src = 'abc'
target = 'cde'
shortest_path = Solution().shortestWay(src, target)
expected = -1
assert shortest_path == expected, f"Expected {expected} but got {shortest_path}"

# Test 5: Source in target, length > 1
src = 'abc'
target = 'abcab'
shortest_path = Solution().shortestWay(src, target)
expected = 2
assert shortest_path == expected, f"Expected {expected} but got {shortest_path}"

# Test 6: Source not in target, length > 1
src = 'abc'
target = 'abcdef'
shortest_path = Solution().shortestWay(src, target)
expected = -1
assert shortest_path == expected, f"Expected {expected} but got {shortest_path}"
