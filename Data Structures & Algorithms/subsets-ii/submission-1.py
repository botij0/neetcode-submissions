class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        self.dfs(nums, result, [], 0)
        return result
    
    def dfs(self, nums: List[int], result: List[List[int]], current:List[int], i: int):
        if i >= len(nums):
            result.append(current.copy())
            return
        
        current.append(nums[i])
        self.dfs(nums, result, current, i+1)
        current.pop()
        
        # Skip same values
        while i + 1 < len(nums) and nums[i] == nums[i+1]:
            i+=1

        self.dfs(nums, result, current, i+1)