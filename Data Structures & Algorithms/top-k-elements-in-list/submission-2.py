class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = {}
        for i in nums:
            if i in result.keys():
                result[i] += 1
            else:
                result[i] = 1
        zoznam = []
        return list(sorted(result, key=lambda k: result[k], reverse=True))[:k]
