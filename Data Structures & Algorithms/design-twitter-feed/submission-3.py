class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list)
        self.following = defaultdict(set)
        self.time = 1

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((-self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        followeeIds = list(self.following[userId]) + [userId]
        tweets = []
        for idx in followeeIds:
            tweets.extend(self.tweets[idx])
       
        heapq.heapify(tweets)

        result = []
        for _ in range(min(len(tweets), 10)):
            result.append(heapq.heappop(tweets)[1])
        return result
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
            self.following[followerId].discard(followeeId)
