class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        result = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    result.append((i, j))
        
        return len(result)