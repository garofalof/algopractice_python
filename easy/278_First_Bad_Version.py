class Solution:
    def firstBadVersion(self, n: int) -> int:
        start, end = 0, n

        while start < end:
            mid = (end - start) // 2 + start

            if isBadVersion(mid):
                end = mid
            else:
                start = mid + 1

        return start


"""
Explanation:

Start with the range of possible bad versions between 0 and n, the total number of versions. In each iteration, calculate the middle value of the current range by adding start and end and dividing the sum by 2. If the middle value is a bad version, update the end value to mid to reduce the range of possible bad versions. On the other hand, if it's not a bad version, update the start value to mid + 1 to move the range to the right. Continue until start is equal to end, which indicates that the first bad version is found. Once done, return the start value.

Notes:

Time complexity: O(log n)

Space complexity: O(1)
"""
