import heapq
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        nums = list(set(nums))
        heapq.heapify(nums)
        count = 1
        max_count = 0
        prvok = None
        while nums:
            actual = heapq.heappop(nums)
            if prvok == None:
                prvok = actual
            elif actual == prvok+1:
                prvok = actual 
                count += 1

            else:
                prvok = actual
                count = 1
            max_count = max(max_count,count)


        return max_count