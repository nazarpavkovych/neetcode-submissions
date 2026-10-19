class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [nums[0]]
        sufix = [nums[-1]]
        dlzka = len(nums)
        for i in range(1,dlzka):
            prefix.append(prefix[i-1]*nums[i])
            sufix.append(sufix[i-1]*nums[-(i+1)])
        result = [sufix[-2]]
        for i in range(1,dlzka-1):
            result.append(sufix[dlzka - 2 - i]* prefix[i-1])
        result.append(prefix[-2])

        return result

