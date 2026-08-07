class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            tosearch = target - nums[i]
            if tosearch in d:
                return [d[tosearch], i]
            
            d[nums[i]] = i
            
        return [-1,-1]

