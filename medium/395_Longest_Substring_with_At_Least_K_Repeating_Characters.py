class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if k == 1:
            return len(s)

        max_unique, max_len = len(set(s)), 0

        for i in range(1, max_unique + 1):
            freq = {}
            start = end = unique = k_count = 0

            while end < len(s):
                if unique <= i:
                    curr_end = s[end]
                    freq[curr_end] = freq.get(curr_end, 0) + 1

                    if freq[curr_end] == k:
                        k_count += 1

                    unique += freq[curr_end] == 1
                    end += 1
                else:
                    curr_start = s[start]
                    freq[curr_start] -= 1

                    if freq[curr_start] == k - 1:
                        k_count -= 1

                    unique -= freq[curr_start] == 0
                    start += 1

                if unique == i and unique == k_count:
                    max_len = max(max_len, end - start)

        return max_len


"""
Explanation:

First, check if k is equal to 1. If it is, the length of s is returned since every character in s appears at least once. Compute the maximum number of unique characters in s. This value is used to limit the maximum number of unique characters in each substring that is checked. Proceed to loop over all possible numbers of unique characters in a substring, from 1 to the maximum number of unique characters in s. For each number of unique characters, use a sliding window approach to find the longest substring that contains only that number of unique characters and has every character appearing at least k times. At each iteration, update the max length with the greater of the length of the sliding window or max length if the unique count == current number of unique characters and unique count == count of characters with frequency == k. Once done, return max length.

Notes:

Time complexity: O(max unique s + length s)

Space complexity: O(1), as we use constant extra space of size 26 to store the unique character count.
"""

# Test 1: k == 1
s = 'abcd'
k = 1
output = Solution().longestSubstring(s, k)
expected = 4
assert output == expected, f"Expected {expected} but got {output}"

# Test 2: k == len(s)
s = 'abcd'
k = 4
output = Solution().longestSubstring(s, k)
expected = 0
assert output == expected, f"Expected {expected} but got {output}"

# Test 3: All characters frequency of k
s = 'aabbccdd'
k = 2
output = Solution().longestSubstring(s, k)
expected = 8
assert output == expected, f"Expected {expected} but got {output}"

# Test 4: No characters frequency of k
s = 'abcd'
k = 2
output = Solution().longestSubstring(s, k)
expected = 0
assert output == expected, f"Expected {expected} but got {output}"

# Test 5: Input string longest substring
s = 'abababab'
k = 2
output = Solution().longestSubstring(s, k)
expected = 8
assert output == expected, f"Expected {expected} but got {output}"

# Test 6: Longest contains character w/ freq < k
s = 'ababbcbdbd'
k = 2
output = Solution().longestSubstring(s, k)
expected = 5
assert output == expected, f"Expected {expected} but got {output}"

# Test 7: len(s) == 1
s = 'a'
k = 1
output = Solution().longestSubstring(s, k)
expected = 1
assert output == expected, f"Expected {expected} but got {output}"

# Test 8: k > len(s)
s = 'a'
k = 2
output = Solution().longestSubstring(s, k)
expected = 0
assert output == expected, f"Expected {expected} but got {output}"

# Test 9: All characters same
s = 'aaaa'
k = 2
output = Solution().longestSubstring(s, k)
expected = 4
assert output == expected, f"Expected {expected} but got {output}"
