class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        self.btrack(nums, result, 0, [])
        return result
    
    def btrack(self, nums: List[int], result: List[List[int]], i:int, current: List[int]):
        if i >= len(nums):
            result.append(current.copy())
            return
        
        current.append(nums[i])
        self.btrack(nums, result, i+1, current)
        current.pop()

        while i + 1 < len(nums) and nums[i] == nums[i+1]:
            i += 1
            
        self.btrack(nums, result, i + 1, current)