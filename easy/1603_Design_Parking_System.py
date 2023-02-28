class ParkingSystem:
    def __init__(self, big: int, medium: int, small: int):
        self.lot = [big, medium, small]

    def addCar(self, carType: int) -> bool:
        idx = carType - 1

        if self.lot[idx]:
            self.lot[idx] -= 1
            return True

        return False


"""
Explanation:

To keep track of the number of available spots, the ParkingSystem class uses a list called lot, where the first element is the number of available spots for large cars, the second element is the number of available spots for medium cars, and the third element is the number of available spots for small cars.

When the addCar method is called, it takes an integer carType as input, representing the type of car that needs to be parked. It then calculates the index of the corresponding element in the lot list by subtracting 1 from carType.

If there is at least one available spot for the given car type, the method decrements the corresponding element in the lot list and returns True to indicate that the car can be parked. Otherwise, the method returns False to indicate that there are no available spots for the given car type.

Notes:

Time Complexity: O(1) for both __init__ and addCar methods, since they both perform constant time operations.

Space Complexity: O(1), since the amount of space used by the class does not increase with the size of the input.
"""

# Test 1: Test initialization
park = ParkingSystem(1, 1, 1)
lot_type = type(park.lot)
expected = type([])
assert lot_type == expected, f"Expected {expected} but got {lot_type}"
car_count = park.lot[0]
expected = 1
assert car_count == expected, f"Expected {expected} but got {car_count}"
car_count = park.lot[1]
expected = 1
assert car_count == expected, f"Expected {expected} but got {car_count}"
car_count = park.lot[2]
expected = 1
assert car_count == expected, f"Expected {expected} but got {car_count}"

# Test 2: Test add car
park = ParkingSystem(1, 1, 1)
can_park = park.addCar(1)
expected = True
assert can_park == expected, f"Expected {expected} but got {can_park}"
can_park = park.addCar(2)
expected = True
assert can_park == expected, f"Expected {expected} but got {can_park}"
can_park = park.addCar(3)
expected = True
assert can_park == expected, f"Expected {expected} but got {can_park}"

# Test 3: Test add car to invalid spot
park = ParkingSystem(1, 1, 1)
can_park = park.addCar(1)
expected = True
assert can_park == expected, f"Expected {expected} but got {can_park}"
can_park = park.addCar(1)
expected = False
assert can_park == expected, f"Expected {expected} but got {can_park}"
can_park = park.addCar(2)
expected = True
assert can_park == expected, f"Expected {expected} but got {can_park}"
can_park = park.addCar(2)
expected = False
assert can_park == expected, f"Expected {expected} but got {can_park}"
can_park = park.addCar(3)
expected = True
assert can_park == expected, f"Expected {expected} but got {can_park}"
can_park = park.addCar(3)
expected = False
assert can_park == expected, f"Expected {expected} but got {can_park}"
