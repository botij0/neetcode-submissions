class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        self.dfs(nums, result, target, 0, [], 0)
        return result

    def dfs(self, nums: List[int], result: List[List[int]], target: int, i:int, curr: List[int], total: int):

        if total == target:
            result.append(curr.copy())
            return

        if i >= len(nums) or total > target:
            return
        
        curr.append(nums[i])
        self.dfs(nums, result, target, i, curr, total + nums[i])
        curr.pop()
        self.dfs(nums, result, target, i+1, curr, total)
