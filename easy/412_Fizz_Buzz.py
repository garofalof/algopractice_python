from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = []

        for i in range(1, n + 1):
            fizz_buzz = [word for num, word in [
                (3, 'Fizz'), (5, 'Buzz')] if not i % num]
            result.append(''.join(fizz_buzz) if fizz_buzz else f'{i}')

        return result

"""
Explanation:

Use list comprehension to check whether i is divisible by either 3 or 5, and create a list of corresponding strings ("Fizz" or "Buzz") using a tuple. Use the join() method to combine the strings in the list into a single string. If the resulting string is empty, append the string representation of the number i to the result list. Once done, return the resulting list of strings.

Notes:

Time complexity: O(n), as we are iterating over the range of 1 to n and performing constant time operations for each iteration.

Space complexity: O(n), as we are creating a list of length n to store the result.
"""

# Test 1: n == 1
n = 1
fizz_buzz = Solution().fizzBuzz(n)
expected = ['1']
assert fizz_buzz == expected, f"Expected {expected} but got {fizz_buzz}"

# Test 2: n == 3
n = 3
fizz_buzz = Solution().fizzBuzz(n)
expected = ['1', '2', 'Fizz']
assert fizz_buzz == expected, f"Expected {expected} but got {fizz_buzz}"

# Test 3: n == 5
n = 5
fizz_buzz = Solution().fizzBuzz(n)
expected = ['1', '2', 'Fizz', '4', 'Buzz']
assert fizz_buzz == expected, f"Expected {expected} but got {fizz_buzz}"

# Test 4: n == 15
n = 15
fizz_buzz = Solution().fizzBuzz(n)
expected = ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz']
assert fizz_buzz == expected, f"Expected {expected} but got {fizz_buzz}"