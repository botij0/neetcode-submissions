class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        if not nums:
            return [[lower, upper]]

        last = lower
        result = []

        if last < nums[0]:
            result.append([lower, nums[0] - 1])
            last = nums[0]

        for i in range(len(nums)):
            if nums[i] > last + 1:
                result.append([last + 1, nums[i] -1])
            
            last = nums[i]
        
        if last < upper:
            result.append([last + 1, upper])
        
        return result


