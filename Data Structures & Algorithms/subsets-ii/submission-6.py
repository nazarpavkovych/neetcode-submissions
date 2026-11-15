class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        def back(i,zoz):
            if i==len(nums):
                res.append(zoz[::])
                return 

            zoz.append(nums[i])
            back(i+1,zoz)
            zoz.pop()

            while i+1<len(nums) and nums[i]==nums[i+1]:
                i+=1
            back(i+1,zoz)
        back(0,[])
        return res