class NestedIterator:
    def __init__(self, nestedList):
        self.list = []
        self.pointer = 0

        self.flattenList(nestedList)

    def flattenList(self, nestedList):
        for item in nestedList:
            if isinstance(item, int):
                self.list.append(item)
            else:
                self.flattenList(item)

    def next(self) -> int:
        if self.hasNext():
            result = self.list[self.pointer]
            self.pointer += 1

            return result

        return None

    def hasNext(self) -> bool:
        return self.pointer < len(self.list)


"""
Explanation:

Create a new list to store the flattened version of the input nested list and initialize a pointer to the beginning of the list. Use a recursive function to flatten the input nested list. In the recursive function, check if each item in the list is an integer, and if so, append it to the new list. If an item is a list, make a recursive call with the sublist as input. When the entire list has been flattened, the `next` method returns the value at the current pointer and increments the pointer. The `hasNext` method returns whether or not the pointer is within the bounds of the flattened list.

Notes:

- Time Complexity: O(n + l) for flattenList, O(1) for next and hasNext. For flattenList, we iterate n times over each list, leaving us with O(n + l) time complexity in the worst case.

- Space Complexity: O(n + d), where n is the space used to store the integers in the nested list, and d is the maximum nesting depth of the input list.
"""

# Test 1: Single element, call next
nested = [1]
iterator = NestedIterator(nested)
next_call = iterator.next()
expected = 1
assert next_call == expected, f"Expected {expected} but got {next_call}"
next_call = iterator.next()
expected = None
assert next_call == expected, f"Expected {expected} but got {next_call}"

# Test 2: Single element, call hasNext
nested = [1]
iterator = NestedIterator(nested)
has_next_call = iterator.hasNext()
expected = True
assert has_next_call == expected, f"Expected {expected} but got {has_next_call}"
iterator.next()
has_next_call = iterator.hasNext()
expected = False
assert has_next_call == expected, f"Expected {expected} but got {has_next_call}"

# Test 2: Flat list
nested = [1, 2, 3]
iterator = NestedIterator(nested)
next_call = iterator.next()
expected = 1
assert next_call == expected, f"Expected {expected} but got {next_call}"
has_next_call = iterator.hasNext()
expected = True
assert has_next_call == expected, f"Expected {expected} but got {has_next_call}"
next_call = iterator.next()
expected = 2
assert next_call == expected, f"Expected {expected} but got {next_call}"
has_next_call = iterator.hasNext()
expected = True
assert has_next_call == expected, f"Expected {expected} but got {has_next_call}"
next_call = iterator.next()
expected = 3
assert next_call == expected, f"Expected {expected} but got {next_call}"
has_next_call = iterator.hasNext()
expected = False
assert has_next_call == expected, f"Expected {expected} but got {has_next_call}"

# Test 2: Nested list
nested = [1, [[2, 3]]]
iterator = NestedIterator(nested)
next_call = iterator.next()
expected = 1
assert next_call == expected, f"Expected {expected} but got {next_call}"
has_next_call = iterator.hasNext()
expected = True
assert has_next_call == expected, f"Expected {expected} but got {has_next_call}"
next_call = iterator.next()
expected = 2
assert next_call == expected, f"Expected {expected} but got {next_call}"
has_next_call = iterator.hasNext()
expected = True
assert has_next_call == expected, f"Expected {expected} but got {has_next_call}"
next_call = iterator.next()
expected = 3
assert next_call == expected, f"Expected {expected} but got {next_call}"
has_next_call = iterator.hasNext()
expected = False
assert has_next_call == expected, f"Expected {expected} but got {has_next_call}"
