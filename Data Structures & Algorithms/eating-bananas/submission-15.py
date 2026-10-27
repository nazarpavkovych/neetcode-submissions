import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maximum = max(piles)

        res = maximum
        l = 1
        r = maximum
        while l<=r:
            k = (l+r)//2
            count = 0
            for i in piles:
                count+=math.ceil(i/k)
            if count<=h:
                res = k
                r = k-1
            else:
                l = k+1
        return res
