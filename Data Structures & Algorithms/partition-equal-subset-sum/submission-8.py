class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        if total % 2 != 0:
            return False
        
        target = total // 2
        # return self.memoization(nums, {}, target, 0)
        return self.dp(nums, target)
    
    def dp(self, nums: List[int], target: int):
        dp = set()
        dp.add(0)

        for i in range(len(nums)-1, -1, -1):
            nextDp = set()
            for val in dp:
                if val + nums[i] == target:
                    return True

                nextDp.add(val + nums[i])
                nextDp.add(val)

            dp = nextDp
        
        return False

    def memoization(self, nums: List[int], cache: dict, target: int, i: int):
        if i >= len(nums) or target < 0:
            return False

        if target == 0:
            return True

        if (target,i) in cache:
            return cache[(target, i)]
        
        cache[(target, i)] = (
            self.memoization(nums, cache, target - nums[i], i + 1) or
            self.memoization(nums, cache, target, i + 1)
        )

        return cache[(target,i)]