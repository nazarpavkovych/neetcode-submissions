class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = {}
        for i in nums:
            if i in result.keys():
                result[i] += 1
            else:
                result[i] = 1
        zoznam = []
        for i,k in sorted(result.items(), key=lambda x: (x[1], x[0]), reverse=True)[:k]:
            zoznam.append(i)
        return zoznam
