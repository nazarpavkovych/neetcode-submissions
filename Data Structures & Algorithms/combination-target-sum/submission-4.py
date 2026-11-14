class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        
        def back(start,zoznam,number):
            if number == target:
                res.append(zoznam)
                return
            for i in range(start,len(nums)):
                if number <= target:
                    back(i,zoznam+[nums[i]],number+nums[i])
        back(0,[],0)
        return res

