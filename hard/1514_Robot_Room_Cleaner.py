class Solution:
    def cleanRoom(self, robot):
        directions = [
            [-1, 0],  # Up
            [0, 1],   # Right
            [1, 0],   # Down
            [0, -1]   # Left
        ]
        visited = set()

        self.backtrack(robot, 0, 0, 0, directions, visited)

    def goBack(self, robot):
        robot.turnRight()
        robot.turnRight()
        robot.move()
        robot.turnRight()
        robot.turnRight()

    def backtrack(self, robot, x, y, d, directions, visited):
        key = (x, y)
        visited.add(key)
        robot.clean()

        for i in range(4):
            nD = (d + i) % 4
            nX = x + directions[nD][0]
            nY = y + directions[nD][1]
            nKey = (nX, nY)

            if nKey not in visited and robot.move():
                self.backtrack(robot, nX, nY, nD, directions, visited)
                self.goBack(robot)

            robot.turnRight()

"""
Explanation:

Initialize the directions list w/ four cardinal directions: Up, Right, Down, and Left. Create an empty set called visited to keep track of visited positions. Call the backtrack method to initiate the DFS traversal, starting from position (0, 0) with an initial direction of 0 (Up).

Inside the backtrack method, create a key representing the current position. Add the key to the visited set. Instruct the robot to clean the current position. Iterate through each of the four directions: calculate the next direction by taking the sum of current direction and current iteration index modulo 4, which allows us to go through the directions in a circular manner. Calculate the next position by adding the corresponding direction values from the directions list to the current position. Create a nKey representing the next position.

If the nKey is not in the visited set and the robot is able to move to the next position, recursively call the backtrack method with the updated position and direction. After the recursive call, instruct the robot to go back to the previous position by calling the goBack method. The goBack method effectively rotates the robot 180 degrees and moves it back to the previous position without changing direction. Instruct the robot to turn right so we can advance to the next direction.

The DFS traversal and cleaning operation then continue until all reachable positions have been visited.

Notes:

Time complexity: O(n - m), where n is the number of nodes and m is the number of obstacles

Space complexity: O(n - m)
"""