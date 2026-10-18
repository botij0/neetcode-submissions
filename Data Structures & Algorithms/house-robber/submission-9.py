class Solution:
    def rob(self, nums: List[int]) -> int:
        x1 = 0
        x2 = 0

        for i in range(len(nums)):
            nums[i] = max(x2, nums[i] + x1)
            x1 = x2
            x2 = nums[i]
        
        return nums[-1]