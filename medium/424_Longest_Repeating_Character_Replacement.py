class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        longest = 0
        left = 0
        maxFreq = 0

        for right in range(len(s)):
            left_char = s[left]
            right_char = s[right]

            count[right_char] = count[right_char] + \
                1 if right_char in count else 1
            maxFreq = max(maxFreq, count[right_char])

            if (right - left + 1 - maxFreq > k):
                count[left_char] -= 1
                left += 1

            longest = max(longest, right - left + 1)

        return longest


"""
Explanation:

Use a sliding window approach to find the solution. Keep a dictionary "count" that keeps track of the frequency of characters in the window, and variables left and right that represent the left and right ends of the window, respectively. Maintain a variable maxFreq that keeps track of the most frequent character in the window.

Iterate over the string from left to right, and at each step add the rightmost character to the window, and update the frequency count and maxFreq. If the size of the window minus the frequency of maxFreq is greater than k, we need to move the window to the right. Decrement the count of the leftmost character, and move the left pointer to the right.

Keep track of the length of the longest substring we have seen so far, and return it at the end of the loop.

Notes:

Time complexity: O(N), where N is the length of the input string s, since we iterate over the string exactly once.

Space complexity: O(1), since the size of the count dictionary is at most 26.
"""

# Test 1: String length == 1, k == 0
repeat_str = 'A'
k = 0
result = Solution().characterReplacement(repeat_str, k)
expected = 1
assert result == expected, f"Expected {expected} but got {result}"

# Test 2: String length == 1, k > 0
repeat_str = 'A'
k = 1
result = Solution().characterReplacement(repeat_str, k)
expected = 1
assert result == expected, f"Expected {expected} but got {result}"

# Test 3: Two different characters, k == 1
repeat_str = 'AB'
k = 1
result = Solution().characterReplacement(repeat_str, k)
expected = 2
assert result == expected, f"Expected {expected} but got {result}"

# Test 4: Same characters, k > 0
repeat_str = 'AAAAA'
k = 3
result = Solution().characterReplacement(repeat_str, k)
expected = 5
assert result == expected, f"Expected {expected} but got {result}"

# Test 6: Different characters, k large enough to replace
repeat_str = 'ABBAA'
k = 2
result = Solution().characterReplacement(repeat_str, k)
expected = 5
assert result == expected, f"Expected {expected} but got {result}"

# Test 7: Different characters, k not large enough to replace
repeat_str = 'ABBAA'
k = 1
result = Solution().characterReplacement(repeat_str, k)
expected = 3
assert result == expected, f"Expected {expected} but got {result}"
