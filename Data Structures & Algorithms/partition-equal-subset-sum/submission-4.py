class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        if total % 2 != 0:
            return False
        
        target = total // 2

        return self.memoization(nums, {}, 0, target)

    
    def memoization(self, nums: List[int], cache: dict, i:int, target: int):
        if target == 0:
            return True
        
        if i >= len(nums) or target < 0:
            return False
        
        if (i, target) in cache:
            return cache[(i, target)]
        
        cache[(i, target)] = (
            self.memoization(nums, cache, i+1, target) or 
            self.memoization(nums, cache, i+1, target - nums[i])
        )

        return cache[(i, target)]