class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        L = 0
        n = len(nums)
        minlenght = float("inf")

        current_sum = 0
        for R in range(n):
            current_sum += nums[R]
            
            while current_sum >= target:
                minlenght = min(R - L + 1, minlenght)
                current_sum -= nums[L]
                L += 1
        
        if minlenght == float("inf"): return 0

        return minlenght
