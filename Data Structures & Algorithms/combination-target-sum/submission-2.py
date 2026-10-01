class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        self.btrack(nums, result, target, 0, [])
        return result

    def btrack(self, nums: List[int], result: List[List[int]], target: int, i: int, current: List[int]):

        if target == 0:
            result.append(current.copy())
            return

        if i >= len(nums) or target < 0:
            return        
        
        current.append(nums[i])
        self.btrack(nums, result, target - nums[i], i, current)
        current.pop()
        self.btrack(nums, result, target, i + 1, current)
