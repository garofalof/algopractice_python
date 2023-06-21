from typing import List


class RLEIterator:

    def __init__(self, encoding: List[int]):
        self.encoding = encoding
        self.index = 0

    def next(self, n: int) -> int:
        while n and self.index < len(self.encoding):
            count = self.encoding[self.index]
            num = self.encoding[self.index + 1]

            if count < n:
                n -= count
                self.index += 2
            else:
                self.encoding[self.index] -= n
                return num

        return -1


"""
Explanation:

Initialize the encoding list and the index variable to keep track of the current position in the encoding. The next method is called to retrieve the next decoded number from the encoding. While the number of elements to retrieve is non-zero and the current position index is within the bounds of the encoding list, perform the following steps: get the count of the next run-length encoded element from the encoding list at the current index. Get the actual number from the encoding list at index + 1. If the count < n, subtract the count from n, move the index two positions forward to the next pair of count and number, and continue the loop. If the count >= n, subtract n from the count, update the count in the encoding list at the current index, and return the number.

If the loop completes without returning a number, it means that the decoding is exhausted, so return -1 to indicate that no more numbers are available.

Notes:

Time complexity: O(1) for objective initialization, O(n) for next method

Space complexity: O(1)
"""

# Test Case 1: Basic decoding
encoding = [3, 8, 2, 10, 1, 3]
iterator = RLEIterator(encoding)
result = []
result.append(iterator.next(2))
result.append(iterator.next(1))
result.append(iterator.next(1))
result.append(iterator.next(4))
result.append(iterator.next(2))
result.append(iterator.next(3))
expected = [8, 8, 10, -1, -1, -1]
assert result == expected, f"Expected {expected} but got {result}"

# Test Case 2: Exhausted decoding
encoding = [1, 1]
iterator = RLEIterator(encoding)
result = iterator.next(1)
expected = 1
assert result == expected, f"Expected {expected} but got {result}"

# Test Case 3: Large n
encoding = [5, 2]
iterator = RLEIterator(encoding)
result = iterator.next(10)
expected = -1
assert result == expected, f"Expected {expected} but got {result}"

# Test Case 4: Empty encoding
encoding = []
iterator = RLEIterator(encoding)
result = iterator.next(1)
expected = -1
assert result == expected, f"Expected {expected} but got {result}"

# Test Case 5: Decoding with multiple zeros
encoding = [0, 5, 0, 3, 0, 2]
iterator = RLEIterator(encoding)
result = []
result.append(iterator.next(3))
result.append(iterator.next(2))
result.append(iterator.next(4))
expected = [-1, -1, -1]
assert result == expected, f"Expected {expected} but got {result}"
