class Solution:
    def merge(self, nums1, m, nums2, n):
        index = m + n - 1
        p1, p2 = m - 1, n - 1

        while p2 >= 0:
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[index] = nums1[p1]
                p1 -= 1
            else:
                nums1[index] = nums2[p2]
                p2 -= 1
            index -= 1

        return nums1


"""
Explanation:

First, the index variable is initialized to m + n - 1, where m and n are the lengths of nums1 and nums2 respectively. This variable represents the index of the last element in the merged sorted array.

Two pointers, p1 and p2, are initialized to m - 1 and n - 1, respectively. These pointers represent the index of the last elements in nums1 and nums2, which are to be compared and merged.

A while loop is then used to compare and merge the elements in nums1 and nums2. The loop continues until p2 is less than 0, indicating that all elements in nums2 have been merged into nums1.

In each iteration of the loop, the element at the current index of nums1 is set to the greater of the corresponding elements at the current indices of nums1 and nums2. If the element at p1 is greater, it is set as the current element in nums1, and p1 is decremented. Otherwise, the element at p2 is set as the current element in nums1, and p2 is decremented.

At the end of the loop, the merged sorted array is contained in nums1, which is returned.

Notes:

Time complexity: O(m + n), where m and n are the lengths of nums1 and nums2, respectively. This is because the algorithm iterates through each element in both arrays once.

Space complexity: O(1), as the algorithm only uses a constant amount of additional memory to store the pointers p1, p2, and index.
"""

# Test 1: One array empty
nums1 = [1, 2, 3]
m = 3
nums2 = []
n = 0
merged = Solution().merge(nums1, m, nums2, n)
expected = [1, 2, 3]
assert merged == expected, f"Expected {expected} but got {merged}"

# Test 2: Second array single element
nums1 = [1, 2, 0]
m = 2
nums2 = [2]
n = 1
merged = Solution().merge(nums1, m, nums2, n)
expected = [1, 2, 2]
assert merged == expected, f"Expected {expected} but got {merged}"

# Test 3: Both arrays have same elements
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [1, 2, 3]
n = 3
merged = Solution().merge(nums1, m, nums2, n)
expected = [1, 1, 2, 2, 3, 3]
assert merged == expected, f"Expected {expected} but got {merged}"

# Test 4: Both arrays unique, nums2 > nums1
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [4, 5, 6]
n = 3
merged = Solution().merge(nums1, m, nums2, n)
expected = [1, 2, 3, 4, 5, 6]
assert merged == expected, f"Expected {expected} but got {merged}"

# Test 5: Both arrays unique, nums2 < nums1
nums1 = [4, 5, 6, 0, 0, 0]
m = 3
nums2 = [1, 2, 3]
n = 3
merged = Solution().merge(nums1, m, nums2, n)
expected = [1, 2, 3, 4, 5, 6]
assert merged == expected, f"Expected {expected} but got {merged}"

# Test 6: Both arrays unique, mixed elements
nums1 = [1, 3, 5, 0, 0, 0]
m = 3
nums2 = [2, 4, 6]
n = 3
merged = Solution().merge(nums1, m, nums2, n)
expected = [1, 2, 3, 4, 5, 6]
assert merged == expected, f"Expected {expected} but got {merged}"
