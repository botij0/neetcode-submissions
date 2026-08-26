class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result, current = [], []
        self.dfs(nums, result, current, 0)
        return result
    
    def dfs(self, nums: List[int], result: List[List[int]], current: List[int], i:int):
        if i >= len(nums):
            result.append(current.copy())
            return

        current.append(nums[i])
        self.dfs(nums, result, current, i+1)
        current.pop()
        self.dfs(nums, result, current, i + 1)
        
        