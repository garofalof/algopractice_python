class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        l = r = 0
        longest = 0
        count = {}

        while r < len(s):
            right = s[r]
            count[right] = r

            while len(count) > k:
                left = s[l]

                if count[left] == l:
                    del count[left]
                l += 1

            longest = max(longest, r - l + 1)

            r += 1

        return longest


"""
Explanation:

Use a sliding window approach to keep track of the longest substring that satisfies the given condition. The count dictionary is used to keep track of the last index where each character appeared in the string. The l and r pointers point to the left and right ends of the current substring being considered. The while loop iterates through the string, and at each iteration, the count dictionary is updated to reflect the latest index of the character that is currently being considered. If the number of distinct characters in the current substring exceeds k, the l pointer is moved to the right until the substring contains at most k distinct characters. The length of the longest substring is updated, and the r pointer is moved to the right. At the end of the loop, reutrn the length of the longest substring that contains at most k distinct characters.

Notes:

Time complexity: O(n), where n is the length of the input string s. This is because we iterate through the string s exactly once with two pointers, and the operations within the loop are constant time.

Space complexity: O(1), since we are keeping track of at most 26 characters in the dictionary.
"""

# Test 1: k == 0
s = 'abcabcabc'
k = 0
longest_length = Solution().lengthOfLongestSubstringKDistinct(s, k)
expected = 0
assert longest_length == expected, f"Expected {expected} but got {longest_length}"

# Test 2: Single character, k == 1
s = 'a'
k = 1
longest_length = Solution().lengthOfLongestSubstringKDistinct(s, k)
expected = 1
assert longest_length == expected, f"Expected {expected} but got {longest_length}"

# Test 3: Single character, k > 1
s = 'a'
k = 2
longest_length = Solution().lengthOfLongestSubstringKDistinct(s, k)
expected = 1
assert longest_length == expected, f"Expected {expected} but got {longest_length}"

# Test 4: Single character repeating, k == 1
s = 'aaaa'
k = 1
longest_length = Solution().lengthOfLongestSubstringKDistinct(s, k)
expected = 4
assert longest_length == expected, f"Expected {expected} but got {longest_length}"

# Test 5: Multiple characters, k == 1
s = 'abcdef'
k = 1
longest_length = Solution().lengthOfLongestSubstringKDistinct(s, k)
expected = 1
assert longest_length == expected, f"Expected {expected} but got {longest_length}"

# Test 6: Multiple characters distinct, k == 2
s = 'abcdef'
k = 2
longest_length = Solution().lengthOfLongestSubstringKDistinct(s, k)
expected = 2
assert longest_length == expected, f"Expected {expected} but got {longest_length}"

# Test 7: Multiple characters repeated, k == 2
s = 'aabccde'
k = 2
longest_length = Solution().lengthOfLongestSubstringKDistinct(s, k)
expected = 3
assert longest_length == expected, f"Expected {expected} but got {longest_length}"

# Test 8: k > length of string
s = 'abc'
k = 5
longest_length = Solution().lengthOfLongestSubstringKDistinct(s, k)
expected = 3
assert longest_length == expected, f"Expected {expected} but got {longest_length}"

# Test 9: k > number of distinct characters
s = 'aabccd'
k = 5
longest_length = Solution().lengthOfLongestSubstringKDistinct(s, k)
expected = 6
assert longest_length == expected, f"Expected {expected} but got {longest_length}"
