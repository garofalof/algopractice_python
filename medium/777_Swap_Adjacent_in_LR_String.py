class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        start_count = start.count('X')
        end_count = end.count('X')

        if start_count != end_count:
            return False

        i = j = 0

        while i < len(start) and j < len(end):
            if start[i] == 'X':
                i += 1
                continue
            if end[j] == 'X':
                j += 1
                continue
            if start[i] != end[j] or (start[i] == 'L' and i < j) or (start[i] == 'R' and i > j):
                return False

            i += 1
            j += 1

        return True


"""
Explanation:

Count the occurrences of the character 'X' in both start and end. If the counts differ, it means there are a different number of 'X' characters in the two strings, making it impossible to transform one into the other. Initialize two pointers, i and j, to keep track of the current positions in start and end, respectively. Iterate through the strings while simultaneously advancing the pointers. If either string has an 'X' at the current position, the pointer is incremented, effectively skipping that character. For non-'X' characters, check if the corresponding characters at the current positions in start and end are equal. If they are not, or if there is a 'L' in start positioned to the right of an 'R', or a 'R' in start positioned to the left of an 'L', it means the transformation is not valid, and the code returns False.

If the code successfully iterates through both strings without encountering any invalid transformations, it returns True, indicating that it is possible to transform start into end.

Notes:

Time complexity: O(n)

Space complexity: O(1)
"""

# Test Case 1: start == 'X' == end
start = "X"
end = "X"
result = Solution().canTransform(start, end)
expected = True
assert result == expected, f"Expected {expected} but got {result}"

# Test Case 2: start == 'L' == end
start = "L"
end = "L"
result = Solution().canTransform(start, end)
expected = True
assert result == expected, f"Expected {expected} but got {result}"

# Test Case 3: start == 'R' == end
start = "R"
end = "R"
result = Solution().canTransform(start, end)
expected = True
assert result == expected, f"Expected {expected} but got {result}"

# Test Case 4: Valid transformation w/ X
start = "RXXLRXRXL"
end = "XRLXXRRLX"
result = Solution().canTransform(start, end)
expected = True
assert result == expected, f"Expected {expected} but got {result}"

# Test Case 5: Invalid transformation w/ X
start = "XLRLR"
end = "RXXLR"
result = Solution().canTransform(start, end)
expected = False
assert result == expected, f"Expected {expected} but got {result}"

# Test Case 6: Invalid transformation w/out X
start = "LLRRLL"
end = "RRLLRR"
result = Solution().canTransform(start, end)
expected = False
assert result == expected, f"Expected {expected} but got {result}"