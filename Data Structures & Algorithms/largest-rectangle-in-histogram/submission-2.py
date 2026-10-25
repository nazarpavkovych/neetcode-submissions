class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maximum = 0
        heights.append(0)
        for i in range(len(heights)):
            index = i
            while stack and stack[-1][1]>heights[i]:
                maximum = max(maximum,stack[-1][1]*(i-stack[-1][0]))
                index= stack[-1][0]
                stack.pop()
            stack.append((index,heights[i]))

        return maximum