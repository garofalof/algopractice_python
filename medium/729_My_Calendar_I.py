class MyCalendar:

    def __init__(self):
        self.cal = [(0, 0), (float('inf'), float('inf'))]

    def book(self, start: int, end: int) -> bool:
        l, r = 0, len(self.cal) - 1

        while l <= r:
            mid = (r - l) // 2 + l

            if end > self.cal[mid][0]:
                l = mid + 1
            elif end < self.cal[mid][0]:
                r = mid - 1
            else:
                l = mid
                break
        if start < self.cal[l - 1][1]:
            return False

        self.cal.insert(l, (start, end))

        return True


"""
Explanation:

The MyCalendar class has an attribute calendar which is initialized with two tuples, (0, 0) and (float('inf'), float('inf')). Each tuple represents a boundary of the calendar, with the first element being the start time and the second element being the end time. The book method takes in a start time start and an end time end, and returns True if the appointment can be booked, and False otherwise. The method uses binary search to find the index to insert the new appointment into the calendar list. If the appointment overlaps with an existing appointment, it returns False. Otherwise, it inserts the new appointment into the calendar list and returns True.

Notes:

Time complexity: O(n), where n is the length of the calendar list, as it takes O(n) time in the worst case to insert an appointment.

Space complexity: O(n), where n is the number of appointments booked in the calendar.
"""

# Test 1: Single valid booking
cal = MyCalendar()
can_book = cal.book(0, 1)
expected = True
assert can_book == expected, f"Expected {expected} but got {can_book}"

# Test 2: Double booking, invalid
cal = MyCalendar()
can_book = cal.book(10, 20)
expected = True
assert can_book == expected, f"Expected {expected} but got {can_book}"
can_book = cal.book(15, 25)
expected = False
assert can_book == expected, f"Expected {expected} but got {can_book}"

# Test 3: Double booking, valid
cal = MyCalendar()
can_book = cal.book(10, 20)
expected = True
assert can_book == expected, f"Expected {expected} but got {can_book}"
can_book = cal.book(25, 30)
expected = True
assert can_book == expected, f"Expected {expected} but got {can_book}"

# Test 4: Double booking, valid, end == start
cal = MyCalendar()
can_book = cal.book(10, 20)
expected = True
assert can_book == expected, f"Expected {expected} but got {can_book}"
can_book = cal.book(20, 30)
expected = True
assert can_book == expected, f"Expected {expected} but got {can_book}"

# Test 5: Test multiple, valid
cal = MyCalendar()
start = 0
end = 10

for _ in range(5):
    can_book = cal.book(start, end)
    expected = True

    assert can_book == expected, f"Expected {expected} but got {can_book}"

    start += 10
    end += 10

# Test 5: Test multiple, invalid
cal = MyCalendar()
can_book = cal.book(10, 20)
expected = True
assert can_book == expected, f"Expected {expected} but got {can_book}"
can_book = cal.book(15, 25)
expected = False
assert can_book == expected, f"Expected {expected} but got {can_book}"
can_book = cal.book(5, 25)
expected = False
assert can_book == expected, f"Expected {expected} but got {can_book}"
