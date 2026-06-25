class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        subsets, curr_set = [], []
        self.helper(0, nums, curr_set, subsets)
        return subsets
    
    def helper(self, i:int, nums: List[int], curr_set: List[int], subsets: List[List[int]]):
        if i >= len(nums):
            subsets.append(curr_set.copy())
            return

        curr_set.append(nums[i])
        self.helper(i+1, nums, curr_set, subsets)


        while i + 1 < len(nums) and nums[i] == nums[i+1]:
            i += 1

        curr_set.pop()
        self.helper(i+1, nums, curr_set, subsets)