from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_palindrome(str):
            return str == str[::-1]

        def dfs(start: int, path: List[str], result: List[List[str]]) -> None:
            if start == len(s):
                result.append(path[:])
                return

            for i in range(start, len(s)):
                partition = s[start: i + 1]

                if is_palindrome(partition):
                    dfs(i + 1, path + [partition], result)

        res = []
        dfs(0, [], res)

        return res


"""
Explanation:

The main function dfs uses a depth-first search approach to recursively generate all possible partitions of s. The function takes three arguments: start, which is the starting index for the current partition; path, which is a list of substrings that are palindromes and make up the current partition; and result, which is a list of all possible partitions of s. The base case for the recursion is when start is equal to the length of s. At this point, we append path to result and return.

For each index i from start to the end of s, we check if the substring s[start:i+1] is a palindrome. If it's a palindrome, we add it to path and recursively call dfs with start set to i+1 and path updated with the new palindrome. After the recursive call, we remove the last added palindrome from path and continue with the next index i.

Finally, we initialize an empty list result and call dfs with start set to 0, path set to an empty list, and result set to the result list. The function dfs populates result with all possible partitions of s, and we return this result at the end of the function.

Notes:

Time complexity: O(n * 2 ^ n), where n is the length of the input string. This is the worst case time complexity when all possible substrings are palindromes. In this case, there could be 2 ^ n possible substrings. For each substring, it takes O(n) to generate the substring and determine if it's a palindrome or not.

Space complexity: O(n), where n is the length of the input string. This space is used on the recursion stack, as the maximum depth of the recursive stack is equal to n in the worst case.
"""

# Test 1: Single character
s = 'a'
partitions = Solution().partition(s)
expected = [['a']]
assert partitions == expected, f"Expected {expected} but got {partitions}"

# Test 2: Multiple characters same
s = 'bb'
partitions = Solution().partition(s)
expected = [['b', 'b'], ['bb']]
assert partitions == expected, f"Expected {expected} but got {partitions}"

# Test 3: No palindromes
s = 'abc'
partitions = Solution().partition(s)
expected = [['a', 'b', 'c']]
assert partitions == expected, f"Expected {expected} but got {partitions}"

# Test 4: Substring palindrome
s = 'aab'
partitions = Solution().partition(s)
expected = [['a', 'a', 'b'], ['aa', 'b']]
assert partitions == expected, f"Expected {expected} but got {partitions}"

# Test 5: Input string palindrome
s = 'racecar'
partitions = Solution().partition(s)
expected = [['r', 'a', 'c', 'e', 'c', 'a', 'r'], [
    'r', 'a', 'cec', 'a', 'r'], ['r', 'aceca', 'r'], ['racecar']]
assert partitions == expected, f"Expected {expected} but got {partitions}"
