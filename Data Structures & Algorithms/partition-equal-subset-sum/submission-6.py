class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        if total % 2 != 0:
            return False
        
        target = total // 2
        return self.memoization(nums, {}, target, 0)

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