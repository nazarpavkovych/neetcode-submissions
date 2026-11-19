class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums)==1:
            return True
        if nums[0]==0:
            return False
        index = len(nums)-1
        dif = 0
        while index>0:
            index-=1
            dif+=1
            if nums[index] >= dif:
                dif = 0

        return dif==0

