class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones)==1:
            return stones[0]
        stones = [-i for i in stones]
        heapq.heapify(stones)
        while len(stones) >= 2:
            x,y = heapq.heappop(stones),heapq.heappop(stones)
            x,y= [abs(x),abs(y)]

            if x < y:
                y-=x
                heapq.heappush(stones,-y)
            if y < x:
                x-=y
                heapq.heappush(stones,-x)
        if len(stones)==1:
            return abs(stones[0])
        else:
            return 0
