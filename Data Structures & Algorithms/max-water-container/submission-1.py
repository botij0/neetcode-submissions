class Solution:
    def maxArea(self, heights: List[int]) -> int:
        L, R = 0, len(heights) - 1

        r = 0
        while L < R:
            current = min(heights[L], heights[R]) * (R - L)
            r = max(r, current)

            if heights[L] > heights[R]:
                R -= 1
            else:
                L += 1
        
        return r
