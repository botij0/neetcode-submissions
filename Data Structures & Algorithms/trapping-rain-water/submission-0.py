class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: 
            return 0

        L, R = 0, len(height) - 1
        result = 0

        leftMax = height[L]
        rightMax = height[R]

        while L < R:
            if leftMax < rightMax:
                L += 1
                leftMax = max(leftMax, height[L])
                result += leftMax - height[L]
            else:
                R -= 1
                rightMax = max(rightMax, height[R])
                result += rightMax - height[R]
            
        return result