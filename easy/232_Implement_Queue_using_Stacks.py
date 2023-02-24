class MyQueue:

    def __init__(self):
        self.input_stack = []
        self.output_stack = []

    def push(self, x: int) -> None:
        self.input_stack.append(x)

    def pop(self) -> int:
        if not self.output_stack:
            while self.input_stack:
                self.output_stack.append(self.input_stack.pop())

        return self.output_stack.pop()

    def peek(self) -> int:
        return self.output_stack[-1] if self.output_stack else self.input_stack[0]

    def empty(self) -> bool:
        return not self.input_stack and not self.output_stack


"""
Explanation:

Create two stacks, s1 and s2, to represent the queue. Implement push, pop, peek, and empty methods. For push, simply add an element to s1. For pop, check if there are any elements in s2 and, if so, pop the top element from s2. Otherwise, pop all the elements from s1 and push them to s2, and then pop the top element from s2. For peek, return the top element of s2 if it's not empty, otherwise return the first element of s1. For empty, return True if both s1 and s2 are empty, otherwise return False.

Notes:

Time Complexity: O(1) for the push, peek, and empty methods. O(n) for the pop method, as we pop all the elements from s1 and push them into s2.

Space Complexity: O(n), as all elements are pushed onto s1 and then onto s2 in the worst case.
"""

# Test 1: Basic operations
q = MyQueue()
q.push(1)
q.push(2)
top = q.peek()
expected = 1
assert top == expected, f"Expected {expected} but got {top}"
popped = q.pop()
expected = 1
assert popped == expected, f"Expected {expected} but got {popped}"
is_empty = q.empty()
expected = False
assert is_empty == expected, f"Expected {expected} but got {is_empty}"
popped = q.pop()
expected = 2
assert popped == expected, f"Expected {expected} but got {popped}"
is_empty = q.empty()
expected = True
assert is_empty == expected, f"Expected {expected} but got {is_empty}"

# Test 2: Push to empty queue
q = MyQueue()
q.push(1)
top = q.peek()
expected = 1
assert top == expected, f"Expected {expected} but got {top}"
popped = q.pop()
expected = 1
assert popped == expected, f"Expected {expected} but got {popped}"
is_empty = q.empty()
expected = True
assert is_empty == expected, f"Expected {expected} but got {is_empty}"

# Test 3: Pop from nonempty queue
q = MyQueue()
q.push(1)
q.push(2)
q.push(3)
popped = q.pop()
expected = 1
assert popped == expected, f"Expected {expected} but got {popped}"
top = q.peek()
expected = 2
assert top == expected, f"Expected {expected} but got {top}"
is_empty = q.empty()
expected = False
assert is_empty == expected, f"Expected {expected} but got {popped}"
popped = q.pop()
expected = 2
assert popped == expected, f"Expected {expected} but got {popped}"
top = q.peek()
expected = 3
assert top == expected, f"Expected {expected} but got {top}"
is_empty = q.empty()
expected = False
assert is_empty == expected, f"Expected {expected} but got {popped}"
popped = q.pop()
expected = 3
assert popped == expected, f"Expected {expected} but got {popped}"
is_empty = q.empty()
expected = True
assert is_empty == expected, f"Expected {expected} but got {popped}"

# Test 4: Push and pop max times
q = MyQueue()

for i in range(100):
    q.push(i)

assert q.peek() == 0, f"Expected 0 but got {q.peek()}"
assert q.empty() == False, f"Expected False but got {q.empty()}"

for i in range(100):
    q.pop()

assert q.empty() == True, f"Expected True but got {q.empty()}"
