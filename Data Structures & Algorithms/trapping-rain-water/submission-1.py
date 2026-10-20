class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        i = 0
        dlzka = len (height)
        prefix = [height[0]]
        sufix = [height[-1]]
        for i in range(1,dlzka):
            prefix.append(max(height[i],prefix[-1]))
        for i in range(dlzka-2,-1,-1):
            sufix.append(max(height[i],sufix[-1]))

        suma = 0
        for i in range(1,dlzka-1):
            suma+= min(prefix[i],sufix[-i-1]) - height[i]
        return suma
