class DetectSquares:
    def __init__(self):
        self.point_count = {}
        self.points = []

    def add(self, point):
        x, y = point

        if x not in self.point_count:
            self.point_count[x] = {}

        self.point_count[x][y] = self.point_count[x].get(y, 0) + 1
        self.points.append(point)

    def count(self, point):
        count = 0
        px, py = point

        for x, y in self.points:
            xDist = abs(px - x)
            yDist = abs(py - y)

            if xDist != yDist or x == px or y == py or px not in self.point_count:
                continue

            count += (self.point_count[x].get(py, 0)
                      * self.point_count[px].get(y, 0))

        return count


"""
Explanation:

The add method takes in a point and adds it to the points list, while also updating the count of that point in the point_count dictionary.

The count method takes in a point and returns the number of valid squares that can be formed with the given point as one of the corners. It does this by iterating over all points in the points list and checking if they can form a valid square with the given point. A square is considered valid if it has sides of equal length and all its corners are points in the points list. If a valid square is found, the method adds to the count variable by multiplying the counts of the two other corners of the square (excluding the given point). The method then returns the final count.

Notes:

Time complexity: O(1) for add method and O(n) for count method.

Space complexity: O(n) for add method and O(1) for count method.
"""

# Test 1: Test add and count w/ 1 point
detect = DetectSquares()
detect.add((0, 0))
square_count = detect.count((0, 0))
expected = 0
assert square_count == expected, f"Expected {expected} but got {square_count}"

# Test 2: Test add and count w/ 2 points
detect = DetectSquares()
detect.add((0, 0))
detect.add((1, 1))
square_count = detect.count((1, 0))
expected = 0
assert square_count == expected, f"Expected {expected} but got {square_count}"

# Test 3: Test add and count w/ 3 points, valid square
detect = DetectSquares()
detect.add((0, 0))
detect.add((1, 1))
detect.add((0, 1))
square_count = detect.count((1, 0))
expected = 1
assert square_count == expected, f"Expected {expected} but got {square_count}"

# Test 4: Test add and count w/ 3 points, invalid square
detect = DetectSquares()
detect.add((0, 0))
detect.add((1, 1))
detect.add((0, 1))
square_count = detect.count((2, 0))
expected = 0
assert square_count == expected, f"Expected {expected} but got {square_count}"

# Test 5: Test multiple points forming squares
detect = DetectSquares()
detect.add((0, 0))
detect.add((1, 1))
detect.add((0, 1))
detect.add((1, 0))
detect.add((2, 2))
detect.add((2, 0))
detect.add((2, 1))
detect.add((0, 2))
detect.add((1, 2))
square_count = detect.count((2, 1))
expected = 2
assert square_count == expected, f"Expected {expected} but got {square_count}"

# Test 6: Test square w/ nonvalid point
detect = DetectSquares()
detect.add((0, 0))
detect.add((1, 1))
detect.add((0, 1))
detect.add((1, 0))
square_count = detect.count((2, 1))
expected = 0
assert square_count == expected, f"Expected {expected} but got {square_count}"

# Test 7: Test multiple squares from same point
detect = DetectSquares()
detect.add((0, 0))
detect.add((1, 1))
detect.add((1, 1))
detect.add((0, 1))
square_count = detect.count((1, 0))
expected = 2
assert square_count == expected, f"Expected {expected} but got {square_count}"
