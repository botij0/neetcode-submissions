class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        for n in nums:
            currPerm = []
            for p in result:
                for i in range(len(p) + 1):
                    copy = p.copy()
                    copy.insert(i, n)
                    currPerm.append(copy)

            result = currPerm

        return result
    
    def btrack(self, nums: List[int], i:int):
        if i >= len(nums):
            return [[]]
        
        result = []
        perms = self.btrack(nums, i+1)
        for p in perms:
            for j in range(len(p) + 1):
                copy = p.copy()
                copy.insert(j, nums[i])
                result.append(copy)

        return result
            
