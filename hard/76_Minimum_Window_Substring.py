from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count_t = Counter(t)
        unique = sum(count_t[char] > 0 for char in count_t)
        have = 0
        l, r = 0, 0
        pointers = (-1, -1)
        shortest = float('inf')
        window = {}

        while r < len(s):
            right = s[r]
            window[right] = window.get(right, 0) + 1

            if window[right] == count_t[right]:
                have += 1
            while have == unique:
                size = r - l + 1
                left = s[l]

                if size < shortest:
                    shortest = size
                    pointers = (l, r)

                window[left] -= 1

                if count_t[left] and window[left] < count_t[left]:
                    have -= 1

                l += 1

            r += 1

        return '' if shortest == float('inf') else s[pointers[0]:pointers[1] + 1]

"""
Explanation:

First, use Counter to count the occurrences of each character in 't' and store it in `count_t`. This helps us keep track of the required count of each character in the window. Next, determine the number of unique characters in `t`. Initialize a map `dictionary` to keep track of the characters in the current window, and a `have` variable to count the number of unique characters we have encountered so far. Set the left and right pointers to 0 and initialize the pointers tuple and shortest to track the minimum window.

Start by moving the right pointer to the right and incrementing the count of the corresponding character in the window dictionary. If the count of the right character in the window matches the required count from count_t, we increment the `have` count. When `have` becomes equal to `unique`, we have found a window containing all the characters from `t`. We calculate the window size and update the pointers and shortest if it is smaller. We then move the left pointer to the right, removing characters from the window. If the removed character is a required character from count_t and its count in the window becomes smaller than the required count, we decrement the `have` count. We then continue moving the right and left pointers until the right pointer reaches the end of the string `s`.

Finally, we return the substring of `s` specified by the pointers, representing the minimum window that contains all characters from `t`. If no such window is found, we return an empty string.

Notes:

Time complexity: O(n + m), where n is the length of string `s` and m is the length of string `t`

Space complexity: O(1), as we store max 26 characters in window or count_t
"""

# Test Case 1: Multiple instances of t in s
s = "ADOBECODEBANC"
t = "ABC"
result = Solution().minWindow(s, t)
expected = "BANC"
assert result == expected, f"Expected {expected} but got {result}"

# Test Case 2: s == t
s = "a"
t = "a"
result = Solution().minWindow(s, t)
expected = "a"
assert result == expected, f"Expected {expected} but got {result}"

# Test Case 3: t not in s, lowercase
s = "a"
t = "aa"
result = Solution().minWindow(s, t)
expected = ""
assert result == expected, f"Expected {expected} but got {result}"

# Test Case 4: t not in s, uppercase
s = "ABCD"
t = "ABCDEF"
result = Solution().minWindow(s, t)
expected = ""
assert result == expected, f"Expected {expected} but got {result}"

# Test Case 5: multiple characters in t in s
s = "aabbcc"
t = "abc"
result = Solution().minWindow(s, t)
expected = "abbc"
assert result == expected, f"Expected {expected} but got {result}"


