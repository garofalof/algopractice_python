class Logger:

    def __init__(self):
        self.times = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        last = self.times.get(message)

        if last is None or timestamp >= last + 10:
            self.times[message] = timestamp
            return True

        return False

"""
Explanation:


Use a dictionary times to store the message and its most recent timestamp. When the shouldPrintMessage method is called, check if the message is already in times. If it's not, add the message to times with its current timestamp. If the message is in times, check if the difference between the current timestamp and the stored timestamp is >= 10. If it is, return False. If the difference is < 10, update the stored timestamp in times to the current timestamp and return True.

Notes:

Time Complexity: O(1)
Space Complexity: O(m), where m is the number of unique messages stored in map
"""