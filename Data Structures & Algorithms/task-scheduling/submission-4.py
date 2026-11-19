class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        slovnik=Counter(tasks)        
        heap = [-i for i in slovnik.values()]
        heapq.heapify(heap)
        time = 0
        queue = deque()
        while heap or queue:
            time +=1
            if heap:
                prvok = heapq.heappop(heap)
                prvok += 1
                if prvok < 0:
                    queue.append([time+n,prvok])
            if  queue and queue[0][0]<=time:
                heapq.heappush(heap,queue.popleft()[1])

            
        return time

        