from typing import List


class Vector2D:

    def __init__(self, vec: List[List[int]]):
        self.list = vec
        self.outer = 0
        self.inner = 0

    def advanceNext(self) -> None:
        while self.outer < len(self.list) and self.inner == len(self.list[self.outer]):
            self.outer += 1
            self.inner = 0

    def next(self) -> int:
        self.advanceNext()

        result = self.list[self.outer][self.inner]
        self.inner += 1

        return result

    def hasNext(self) -> bool:
        self.advanceNext()

        return self.outer < len(self.list)


"""
Explanation:

Initialize the vector class by setting the list to the nested input list, while also setting inner and outer pointers to 0.

advanceNext: Skip sublists that are already exhausted. Increment both outer and inner until a valid sublist is found, or outer becomes equal to the length of the nested list.

next: Call advanceNext to find the next valid sublist, then get the current element and increment the inner index by 1 for the next call. Once done, return the current element.

hasNext: Call advanceNext to find the next valid sublist, then return whether outer is < length of the nested list.

Notes:

Time complexity: O(1) for next and hasNext. O(v / n) for advanceNext, where v is the total number of elements in the nested list vec and n is the number of inner lists. If the iterator is completely exhausted, then all calls to advanceNext will have performed O(n + v) total operations. However, because we perform n advanceNext operations in order to exhaust the iterator, the amortized cost of this operation is O((n + v) / n), or O(v / n).

Space complexity: O(1)
"""

# Test 1: Regular case
vec = [[1, 2], [3], [4]]
vector = Vector2D(vec)
next = vector.next()
has_next = vector.hasNext()
assert next == 1, f"Expected 1 but got {next}"
assert has_next == True, f"Expected True but got {has_next}"
next = vector.next()
has_next = vector.hasNext()
assert next == 2, f"Expected 2 but got {next}"
assert has_next == True, f"Expected True but got {has_next}"
next = vector.next()
has_next = vector.hasNext()
assert next == 3, f"Expected 3 but got {next}"
assert has_next == True, f"Expected True but got {has_next}"
next = vector.next()
has_next = vector.hasNext()
assert next == 4, f"Expected 4 but got {next}"
assert has_next == False, f"Expected False but got {has_next}"

# Test 2: Empty list
vec = []
vector = Vector2D(vec)
has_next = vector.hasNext()
assert has_next == False, f"Expected False but got {has_next}"

# Test 3: Single element in list
vec = [[1]]
vector = Vector2D(vec)
next = vector.next()
has_next = vector.hasNext()
assert next == 1, f"Expected 1 but got {next}"
assert has_next == False, f"Expected False but got {has_next}"

# Test 4: Multiple elements in single inner list
vec = [[1, 2, 3, 4]]
vector = Vector2D(vec)
next = vector.next()
assert next == 1, f"Expected 1 but got {next}"
next = vector.next()
assert next == 2, f"Expected 2 but got {next}"
next = vector.next()
assert next == 3, f"Expected 3 but got {next}"
next = vector.next()
assert next == 4, f"Expected 4 but got {next}"
has_next = vector.hasNext()
assert has_next == False, f"Expected False but got {has_next}"
