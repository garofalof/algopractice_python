class Solution:
    def findCelebrity(self, n: int) -> int:
        celebrity = 0

        for i in range(n):
            if knows(celebrity, i):
                celebrity = i
        for i in range(n):
            if (i != celebrity and knows(celebrity, i)) or not knows(i, celebrity):
                return -1

        return celebrity


"""
Explanation:

Initialize the celebrity variable to 0. Loop through all the people in the party, starting from 0 to n-1. If the current person knows the celebrity, update the celebrity variable to the current person. Loop through all the people in the party again, starting from 0 to n-1.
If the current person isn't the celebrity and the celebrity knows the current person, or the current person doesn't know the celebrity, return -1. Otherwise, return the celebrity.

Notes:

Time complexity: O(n), as we run two loops of size n to find the celebrity.

Space complexity: O(1), as we use constant extra space to hold the celebrity pointer.
"""
