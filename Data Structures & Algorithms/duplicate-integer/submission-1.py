class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        zoznam = set()
        for i in range(len(nums)):
            if nums[i] not in zoznam:
                zoznam.add(nums[i])
            else:
                return True
        return False