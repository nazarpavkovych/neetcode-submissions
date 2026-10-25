class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:  
        for i in range(len(position)):
            position[i] = (position[i],speed[i])
        position.sort()
        stack = []
        n = 1
        for i in position:
            stack.append((target-i[0])/i[1])
        result = 0
        while stack:
            auto = stack.pop()
            while stack and auto>=stack[-1]:
                stack.pop()
            result+=1
            
        return result


        