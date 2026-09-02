class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list)
        self.followers = defaultdict(set)
        self.recent = -1

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.recent, tweetId))
        self.recent -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        users = [userId] + list(self.followers[userId])
        allTweets = []

        for uid in users:
            allTweets.extend(self.tweets[uid])

        heapq.heapify(allTweets)
        result = []

        for _ in range(min(len(allTweets), 10)):
            result.append(heapq.heappop(allTweets)[1])

        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].discard(followeeId)
