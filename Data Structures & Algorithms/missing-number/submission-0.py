class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        r = 0
        for i in range(1, len(nums)+1):
            r += i

        for n in nums:
            r -= n

        return r