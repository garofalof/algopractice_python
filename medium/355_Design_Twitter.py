import heapq
from collections import defaultdict
from typing import List


class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)
        self.users = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append([self.time, tweetId])
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        result = []
        heap = []

        self.users[userId].add(userId)

        for followeeId in self.users[userId]:
            if followeeId in self.tweets:
                index = len(self.tweets[followeeId]) - 1
                time, tweetId = self.tweets[followeeId][index]
                heap.append([time, tweetId, followeeId, index - 1])

        heapq.heapify(heap)

        while heap and len(result) < 10:
            time, tweetId, followeeId, index = heapq.heappop(heap)
            result.append(tweetId)

            if index >= 0:
                time, tweetId = self.tweets[followeeId][index]
                heapq.heappush(heap, [time, tweetId, followeeId, index - 1])

        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        self.users[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.users[followerId]:
            self.users[followerId].remove(followeeId)


"""
Explanation:

Initialize the Twitter class by setting the time to 0, creating an empty map tweets, and creating an empty map users to store the users and their followee relationships.

postTweet: Allows a user to post a tweet. Append to the tweets map using the user's id as the key and a list of time and tweet id as value. Decrement time by 1 each time a tweet is posted.

getNewsFeed: Returns the 10 most recent tweets from a user's following list. Add the user's id to the users map. Loop through each followee of the user, checking if the followee has any tweets. If so, add the most recent tweet to heap. Transform the heap into a min heap using the heapify method. While our heap has values and result list lenth < 10, pop the tweet with the lowest time value from the heap, adds it to the result list, and continue to pop and add tweets to the result list until either the heap is empty or the result list has 10 tweets. If there are still tweets from current followee, add the next tweet to the heap before the while loop continues.

follow: Allows a user to follow another user. Add the followee's id to the set of followees stored in the users map for the specified user.

unfollow: Allows a user to unfollow another user. If the followee's id is in the set of followees stored in the users map for the specified user, it removes the followee's id from that set.

Notes:

Time complexity: O(1) for postTweet, follow, and unfollow. O(k) for getNewsFeed, where k is the number of tweets in original heap.
Space complexity: O(n), where n is the number of tweets posted by all users.
"""

# Test 1: test single user postTweet and getNewsFeed functionality
twitter = Twitter()
twitter.postTweet(1, 1)
twitter.postTweet(1, 2)
feed = twitter.getNewsFeed(1)
assert feed == [2, 1], f"Expected [2, 1] but got {feed}"

# Test 2: test multiple user postTweet and getNewsFeed functionality
twitter = Twitter()
twitter.postTweet(1, 1)
twitter.postTweet(2, 2)
twitter.postTweet(2, 3)
twitter.follow(1, 2)
feed = twitter.getNewsFeed(1)
assert feed == [3, 2, 1], f"Expected [3, 2, 1] but got {feed}"

# Test 3: test follow / unfollow functionality
twitter = Twitter()
twitter.postTweet(1, 1)
twitter.postTweet(2, 2)
twitter.follow(1, 2)
feed = twitter.getNewsFeed(1)
assert feed == [2, 1], f"Expected [2, 1] but got {feed}"
twitter.unfollow(1, 2)
feed = twitter.getNewsFeed(1)
assert feed == [1], f"Expected [1] but got {feed}"

# Test 4: test >10 tweets
twitter = Twitter()

for i in range(1, 12):
    twitter.postTweet(1, i)

feed = twitter.getNewsFeed(1)
assert feed == [11, 10, 9, 8, 7, 6, 5, 4, 3,
                2], f"Expected [11, 10, 9, 8, 7, 6, 5, 4, 3, 2] but got {feed}"
