class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        vzd = []
        for i in range(len(points)):
            x_d = points[i][0]**2
            y_d = points[i][1]**2
            vzd.append([(x_d+y_d)**(0.5),i])
        heapq.heapify(vzd)

        res_idx = []
        for i in range(k):
            res_idx.append(points[heapq.heappop(vzd)[1]])
        return res_idx

