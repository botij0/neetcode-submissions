class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        if total % 2 != 0:
            return False
        
        target = total // 2

        # return self.memoization(nums, {}, 0, target)
        return self.dpSol(nums, target)    

    def dpSol(self, nums: List[int], target: int) -> bool:
        dp = set()
        dp.add(0)

        for i in range(len(nums) - 1, -1, -1):
            nextDp = set()
            for t in dp:
                if t + nums[i] == target:
                    return True

                nextDp.add(t + nums[i])
                nextDp.add(t)
            
            dp = nextDp

        return False

    
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