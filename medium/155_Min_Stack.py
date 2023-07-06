class MinStack:

    def __init__(self):
        self.stack = []
        self.min = []

    def push(self, val: int) -> None:
        if not len(self.min) or val <= self.getMin():
            self.min.append(val)

        self.stack.append(val)

    def pop(self) -> None:
        val = self.stack.pop()

        if val == self.getMin():
            self.min.pop()

        return val

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min[-1]

"""
Explanation:

The __init__ method initializes two lists: stack to store the elements in the stack and min to store the minimum elements encountered so far. The push method takes an integer value as input and adds it to the stack. If the min list is empty or the new value <= the current minimum value, the new value is also added to the min list. The pop method removes and returns the top element from the stack. If the removed element is equal to the current minimum value, it is also removed from the min list. The top method returns the top element of the stack without modifying the stack. The getMin method returns the current minimum value stored in the min list.

Notes:

Time complexity: O(1) for all operations

Space complexity: O(n), as we store n number of items pushed to stack
"""

# Test Case 1: Basic Operations
stack = MinStack()
stack.push(1)
stack.push(2)
top = stack.top()
expected = 2
assert top == expected, f"Expected {expected} but got {top}"
min = stack.getMin()
expected = 1
assert min == expected, f"Expected {expected} but got {min}"
popped = stack.pop()
expected = 2
assert popped == expected, f"Expected {expected} but got {popped}"
popped = stack.pop()
expected = 1
assert popped == expected, f"Expected {expected} but got {popped}"

# Test Case 2: Increasing values
stack = MinStack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
top = stack.top()
min = stack.getMin()
expected_top = 5
expected_min = 1
assert top == expected_top, f"Expected {expected_top} but got {top}"
assert min == expected_min, f"Expected {expected_min} but got {min}"

# Test Case 3: Decreasing values
stack = MinStack()
stack.push(5)
stack.push(4)
stack.push(3)
stack.push(2)
stack.push(1)
top = stack.top()
min = stack.getMin()
expected_top = 1
expected_min = 1
assert top == expected_top, f"Expected {expected_top} but got {top}"
assert min == expected_min, f"Expected {expected_min} but got {min}"

# Test Case 4: Equal values
stack = MinStack()
stack.push(1)
stack.push(1)
stack.push(1)
stack.push(1)
stack.push(1)
top = stack.top()
min = stack.getMin()
expected_top = 1
expected_min = 1
assert top == expected_top, f"Expected {expected_top} but got {top}"
assert min == expected_min, f"Expected {expected_min} but got {min}"

# Test Case 5: Mixed values
stack = MinStack()
stack.push(5)
stack.push(1)
stack.push(3)
stack.push(2)
stack.push(4)
top = stack.top()
min = stack.getMin()
expected_top = 4
expected_min = 1
assert top == expected_top, f"Expected {expected_top} but got {top}"
assert min == expected_min, f"Expected {expected_min} but got {min}"
