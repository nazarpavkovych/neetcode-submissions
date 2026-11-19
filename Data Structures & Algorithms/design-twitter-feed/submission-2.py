class Twitter:

    def __init__(self):
        self.heap = []
        self.subs = dict()
        self.sub_post = dict()
        self.time = 0

        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time-=1
        if userId in self.sub_post.keys():
            self.sub_post[userId].append([self.time,tweetId])
        else:
            self.sub_post[userId]= [[self.time,tweetId]]

        

    def getNewsFeed(self, userId: int) -> List[int]:
        if userId in self.sub_post:
            zoznam = self.sub_post[userId][:]
        else:
            zoznam = []
        if userId in self.subs.keys():
            for i in self.subs[userId]:
                zoznam += self.sub_post[i][:]
        heapq.heapify(zoznam)
        k = 10
        news = []
        while zoznam and k > 0:
            k-=1
            news.append(heapq.heappop(zoznam)[1])
        return news

        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.subs.keys():
            self.subs[followerId] = {followeeId}
        else:
            self.subs[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.subs[followerId].discard(followeeId)

        
