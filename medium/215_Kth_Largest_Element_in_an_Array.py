from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k

        def quickSelect(l, r):
            pivot = nums[r]
            pointer = l

            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[i], nums[pointer] = nums[pointer], nums[i]
                    pointer += 1

            nums[pointer], nums[r] = nums[r], nums[pointer]

            if pointer > k:
                return quickSelect(l, pointer - 1)
            elif pointer < k:
                return quickSelect(pointer + 1, r)
            else:
                return nums[pointer]

        return quickSelect(0, len(nums) - 1)


"""
Explanation:

Start by subtracting k from the length of the input list to find the index of the kth largest element in a sorted list. Define a recursive function, quickSelect, that takes the left and right indices of the current partition. Inside the function, set the pivot as the last element of the current partition, and initialize the pointer to the left index. Then iterate over the elements in the partition, swapping them with the pointer if they are <= pivot, and incrementing the pointer. Once the iteration is complete, the pivot is swapped with the element at the pointer, which puts the pivot in its final position in the sorted list.

After that, check if the pointer > index of the kth largest element. If it is, recursively call quickSelect on the left partition. If < index of the kth largest element, recursively call quickSelect on the right partition. If == to the index of the kth largest element, return the element at the pointer, which is the kth largest element.

Finally, calls quickSelect with the left and right indices of the whole list, and return the result.

Notes:

Time complexity: O(n) in the average case and O(n^2) in the worst case, where n is the length of the input list. The worst case for time complexity is when the input list is already sorted in ascending or descending order. In this case, the partitioning always selects the last element as the pivot, which would result in a partition of size n-1 and another partition of size 1 in each recursive call. This would result in a total of n-1 recursive calls, with each call taking O(n) time for partitioning, making the worst case time complexity O(n^2). However, the average case time complexity for Quickselect is O(n), assuming the elements in the input list are randomly distributed. This is because on average, the partitioning would result in two partitions of roughly equal sizes, leading to roughly halving the remaining elements in each recursive call.

Space complexity: O(log n) due to the call stack. Each recursive call splits the array into two smaller subarrays, so the maximum depth of the call stack is log n.
"""

# Test 1: k == 1, len(nums) == 1
nums = [5]
k = 1
kth_largest = Solution().findKthLargest(nums, k)
expected = 5
assert kth_largest == expected, f"Expected {expected} but got {kth_largest}"

# Test 2: k == 1, len(nums) > 1
nums = [1, 3, 2, 5]
k = 1
kth_largest = Solution().findKthLargest(nums, k)
expected = 5
assert kth_largest == expected, f"Expected {expected} but got {kth_largest}"

# Test 3: k == len(nums)
nums = [1, 3, 2, 5]
k = 4
kth_largest = Solution().findKthLargest(nums, k)
expected = 1
assert kth_largest == expected, f"Expected {expected} but got {kth_largest}"

# Test 4: All nums same
nums = [5, 5, 5, 5]
k = 2
kth_largest = Solution().findKthLargest(nums, k)
expected = 5
assert kth_largest == expected, f"Expected {expected} but got {kth_largest}"

# Test 5: All nums descending
nums = [4, 3, 2, 1]
k = 2
kth_largest = Solution().findKthLargest(nums, k)
expected = 3
assert kth_largest == expected, f"Expected {expected} but got {kth_largest}"

# Test 6: All nums ascending
nums = [1, 2, 3, 4]
k = 3
kth_largest = Solution().findKthLargest(nums, k)
expected = 2
assert kth_largest == expected, f"Expected {expected} but got {kth_largest}"
