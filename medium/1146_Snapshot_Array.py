class SnapshotArray:
    def __init__(self, length):
        self.id = 0
        self.data = [[] for _ in range(length)]

    def set(self, index, val):
        self.data[index].append([val, self.id])

    def snap(self):
        self.id += 1
        return self.id - 1

    def get(self, index, snap_id):
        data = self.data[index]
        left, right = 0, len(data) - 1
        i = -1

        while left <= right:
            mid = left + (right - left) // 2

            if data[mid][1] <= snap_id:
                i = mid
                left = mid + 1
            else:
                right = mid - 1

        return data[i][0] if i != -1 else 0


"""
Explanation:

Initializes the class by setting the initial id to 0 and creating an empty list for each index of the array. The `set` method takes an index and a value and appends a pair of the value and the current ID to the list at the given index. The `snap` method increments the ID by 1 and returns the previous ID, which serves as the snapshot identifier. The `get` method takes an index and a snapshot ID and retrieves the value associated with the index at or before the given snapshot ID. It performs a binary search on the list at the given index to find the value associated with the closest preceding snapshot ID.

Notes:

- Time complexity: O(n) for initialization, O(1) for set and snap, and O(log n) for get.
- Space complexity: O(n + k), where n is the array size and k is the number of pairs saved in the array.
"""

# Test 1: Basic set, snap, and get operations
array = SnapshotArray(5)
array.set(0, 10)
array.set(1, 20)
array.set(2, 30)
snap_id_1 = array.snap()
array.set(0, 15)
snap_id_2 = array.snap()
array.set(2, 35)
val_1 = array.get(0, snap_id_1)
val_2 = array.get(1, snap_id_1)
val_3 = array.get(2, snap_id_1)
val_4 = array.get(0, snap_id_2)
val_5 = array.get(2, snap_id_2)

assert val_1 == 10, f"Expected {10} but got {val_1}"
assert val_2 == 20, f"Expected {20} but got {val_2}"
assert val_3 == 30, f"Expected {30} but got {val_3}"
assert val_4 == 15, f"Expected {15} but got {val_4}"
assert val_5 == 30, f"Expected {30} but got {val_5}"


# Test 2: Setting values and snapping multiple times
array = SnapshotArray(3)
array.set(0, 100)
array.set(1, 200)
snap_id_1 = array.snap()
array.set(0, 150)
snap_id_2 = array.snap()
array.set(2, 300)
snap_id_3 = array.snap()
array.set(1, 250)
snap_id_4 = array.snap()
array.set(2, 350)
val_1 = array.get(0, snap_id_1)
val_2 = array.get(1, snap_id_1)
val_3 = array.get(2, snap_id_1)
val_4 = array.get(0, snap_id_2)
val_5 = array.get(2, snap_id_2)
val_6 = array.get(0, snap_id_3)
val_7 = array.get(1, snap_id_3)
val_8 = array.get(2, snap_id_3)
val_9 = array.get(0, snap_id_4)
val_10 = array.get(1, snap_id_4)
val_11 = array.get(2, snap_id_4)

assert val_1 == 100, f"Expected {100} but got {val_1}"
assert val_2 == 200, f"Expected {200} but got {val_2}"
assert val_3 == 0, f"Expected {0} but got {val_3}"
assert val_4 == 150, f"Expected {150} but got {val_4}"
assert val_5 == 0, f"Expected {0} but got {val_5}"
assert val_6 == 150, f"Expected {150} but got {val_6}"
assert val_7 == 200, f"Expected {200} but got {val_7}"
assert val_8 == 300, f"Expected {300} but got {val_8}"
assert val_9 == 150, f"Expected {150} but got {val_9}"
assert val_10 == 250, f"Expected {250} but got {val_10}"
assert val_11 == 300, f"Expected {300} but got {val_11}"
