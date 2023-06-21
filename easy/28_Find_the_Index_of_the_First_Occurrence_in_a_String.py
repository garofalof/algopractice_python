class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0

        m, n = len(haystack), len(needle)

        for i in range(m - n + 1):
            if haystack[i:i + n] == needle:
                return i

        return -1

"""
Explanation:

If needle is an empty string, return 0 as needle is considered to be found at the beginning of haystack. Get the lengths of haystack and needle and assign them to variables m and n, respectively. Iterate through m - n + 1 possible starting indices in haystack using the outer loop. Check if the substring of haystack starting from the current index and having a length of n matches needle.

If the substring matches needle, return the current index as the first occurrence of needle in haystack.
If no match is found after the iterations, return -1 to indicate that needle is not present in haystack.

Notes:

Time complexity: O(m * n), where m and n are the respective lenghts of the input strings

Space complexity: O(1)
"""

# Test Case 1: Empty needle
haystack = "hello"
needle = ""
result = Solution().strStr(haystack, needle)
expected = 0
assert result == expected, f"Expected {expected} but got {result}"

# Test Case 2: Needle is present at the beginning of haystack
haystack = "hello"
needle = "he"
result = Solution().strStr(haystack, needle)
expected = 0
assert result == expected, f"Expected {expected} but got {result}"

# Test Case 3: Needle is present at the end of haystack
haystack = "hello"
needle = "lo"
result = Solution().strStr(haystack, needle)
expected = 3
assert result == expected, f"Expected {expected} but got {result}"

# Test Case 4: Needle is present in the middle of haystack
haystack = "hello"
needle = "ll"
result = Solution().strStr(haystack, needle)
expected = 2
assert result == expected, f"Expected {expected} but got {result}"

# Test Case 5: Needle is not present in haystack
haystack = "hello"
needle = "abc"
result = Solution().strStr(haystack, needle)
expected = -1
assert result == expected, f"Expected {expected} but got {result}"

# Test Case 6: Needle is longer than haystack
haystack = "hello"
needle = "hello world"
result = Solution().strStr(haystack, needle)
expected = -1
assert result == expected, f"Expected {expected} but got {result}"

# Test Case 7: Needle is equal to haystack
haystack = "hello"
needle = "hello"
result = Solution().strStr(haystack, needle)
expected = 0
assert result == expected, f"Expected {expected} but got {result}"

# Test Case 8: Empty haystack
haystack = ""
needle = "hello"
result = Solution().strStr(haystack, needle)
expected = -1
assert result == expected, f"Expected {expected} but got {result}"
