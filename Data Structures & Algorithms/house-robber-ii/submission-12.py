class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
            
        return max(
            self.aux(nums[0:len(nums)-1]),
            self.aux(nums[1:])
        )
    
    def aux(self, nums: List[int]):
        x1 = 0
        x2 = 0

        for i in range(len(nums)):
            nums[i] = max(x2, x1 + nums[i])
            x1 = x2
            x2 = nums[i]
        
        return nums[-1]
