class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        zoznam = []
        dlzka = len(nums)
        for i in range(dlzka-2):
            target = -nums[i]
            j = i+1
            k = dlzka - 1
            while j < k:
                if nums[k]+nums[j]> target:
                    k-=1
                if nums[j] + nums[k] < target:
                    j+=1
                if nums[j] + nums[k] == target:
                    if i!= j  and i != k and j != k:
                        zoznam.append((nums[i],nums[j],nums[k]))
                    j+=1
        return [list(i) for i in list(set(zoznam))]
                     

