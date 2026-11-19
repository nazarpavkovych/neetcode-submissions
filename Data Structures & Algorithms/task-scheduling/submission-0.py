class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        slovnik = dict()
        for i in tasks:
            if i in slovnik.keys():
                slovnik[i] -= 1
            else:
                slovnik[i] = -1
        heap = list(slovnik.values())
        heapq.heapify(heap)
        time = 0
        queue = []
        while heap or queue:
            time +=1
            if heap:
                prvok = heapq.heappop(heap)
                prvok += 1
                if prvok < 0:
                    heapq.heappush(queue,[time+n,prvok])
            while  queue and queue[0][0]<=time:
                heapq.heappush(heap,heapq.heappop(queue)[1])

            
        return time

        