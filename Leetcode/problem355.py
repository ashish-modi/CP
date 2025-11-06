# Leetcode Problem 355: Design Twitter
# Difficulty: Medium
# URL: https://leetcode.com/problems/design-twitter/

class Twitter:

    def __init__(self):
        self.user_dict = defaultdict(list)
        self.tweets = defaultdict(list)
        self.tweet_count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId] = self.tweets.get(userId,[]) + [(self.tweet_count, tweetId)]
        self.tweet_count -=1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        
        res = []
        count = 0
        
        for time, tweet in self.tweets[userId][-10:]:
            heapq.heappush(heap, (time, tweet))

        for followee in self.user_dict[userId]:
            for time, tweet in self.tweets[followee][-10:]:
                heapq.heappush(heap, (time, tweet))

        for _ in range(min(10, len(heap))):
            time, tweet = heapq.heappop(heap)
            res.append(tweet)

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
     
        if(followerId != followeeId) and (followeeId not in self.user_dict[followerId]):
            self.user_dict[followerId].append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
    
        if followeeId in self.user_dict[followerId]:
            self.user_dict[followerId].pop(self.user_dict[followerId].index(followeeId))


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)

# Time complexity:
# postTweet: O(1) - Appending a tweet to the user's tweet list takes constant time.
# getNewsFeed: O(N log N) - Where N is the total number of tweets considered (from the user and their followees). Each tweet is pushed into a min-heap, which takes log N time.
# follow: O(1) - Appending a followee to the user's followee list takes constant time.
# unfollow: O(M) - Where M is the number of followees the user has, as we may need to search through the list to find the followee to remove.
# Space complexity:
# O(U + T) - Where U is the number of users and T is the total number of tweets. We store followee relationships and tweets for each user.
# Explanation:
# The Twitter class uses dictionaries to maintain user follow relationships and their tweets.
# Each tweet is stored with a timestamp to facilitate ordering in the news feed.
# The getNewsFeed method uses a min-heap to efficiently retrieve the 10 most recent tweets from the user and their followees.
# The follow and unfollow methods manage the follow relationships between users.

