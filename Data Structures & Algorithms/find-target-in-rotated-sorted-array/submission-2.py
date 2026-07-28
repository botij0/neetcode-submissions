class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target < nums[0]:
            for i in range(len(nums)-1, -1, -1):
                if nums[i] == target:
                    return i
                
                if nums[i] < target:
                    return -1
        else:
            for i in range(len(nums)):
                if nums[i] == target:
                    return i
                
                if nums[i] > target:
                    return -1
        
        return -1