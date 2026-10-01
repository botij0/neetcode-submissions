class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.btrack(nums, result, 0, [])
        return result
    
    def btrack(self, nums: List[int], result: List[List[int]], i: int, current: List[int]):
        if i >= len(nums):
            result.append(current.copy())
            return
        
        current.append(nums[i])
        self.btrack(nums, result, i + 1, current)
        current.pop()
        self.btrack(nums, result, i + 1, current)