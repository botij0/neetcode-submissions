class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        x2 = len(nums)
        for i in range(len(nums)):
            x2 ^= i ^ nums[i]
        
        return x2