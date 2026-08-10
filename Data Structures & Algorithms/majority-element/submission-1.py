class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        result = nums[0]

        for n in nums:
            if count == 0:
                result = n
            
            if result == n:
                count += 1
            else:
                count -= 1

        return result