class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        result = 0

        for i in range(len(heights)):
            start = i
            while stack and stack[-1][1] > heights[i]:
                (j, h) = stack.pop()
                result = max(result, h * (i-j))
                start = j             

            stack.append((start, heights[i]))
        
        while stack:
            (j, h) = stack.pop()
            result = max(result, h * (len(heights) - j)) 
        
        return result