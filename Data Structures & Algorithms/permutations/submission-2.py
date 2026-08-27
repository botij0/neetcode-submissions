class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return self.dfs(nums, 0)

    def dfs(self, nums: List[int], i: int):
        if i >= len(nums):
            return [[]]
        
        result = []
        perms = self.dfs(nums, i+1)
        for p in perms:
            for j in range(len(p) + 1):
                copy = p.copy()
                copy.insert(j, nums[i])
                result.append(copy)

        return result
    
    def iterative(self, nums: List[int]) -> List[List[int]]:
        perms = [[]]

        for n in nums:
            current = []
            for p in perms:
                for i in range(len(p) + 1):
                    copy = p.copy()
                    copy.insert(i, n)
                    current.append(copy)
            perms = current
        
        return perms