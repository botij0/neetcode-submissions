class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        all_sum = sum(nums)
        if all_sum % 2 == 1:
            return False

        target = all_sum // 2
        dp = set()
        dp.add(0)
        
        for i in range(len(nums) -1, -1, -1):
            nextDp = set()
            for t in dp:
                if (t + nums[i]) == target:
                    return True
                
                nextDp.add(t + nums[i])
                nextDp.add(t)
            
            dp = nextDp

        return target in dp
    
    # def memoization(self, nums: List[int]) -> bool:
    #     all_sum = sum(nums)
    #     if all_sum % 2 == 1:
    #         return False

    #     target = all_sum // 2
    #     n = len(nums)
    #     cache = [[-1] * (target + 1) for _ in range(n + 1)]

    #     return self.helper(0,nums, target, cache)

    # def helper(self, 
    #     i:int,
    #     nums: List[int],
    #     target: int,
    #     cache: List[List[int | bool]]
    # ) -> bool:
        
    #     if target == 0:
    #         return True
        
    #     if i>= len(nums) or target < 0:
    #         return False
        
    #     if cache[i][target] != -1:
    #         return cache[i][target]

    #     cache[i][target] = (self.helper(i+ 1, nums, target, cache) 
    #                         or
    #                         self.helper(i + 1, nums, target - nums[i], cache))
        
    #     return cache[i][target]
        


        
