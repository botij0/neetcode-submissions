class Solution:
    def findMin(self, nums: List[int]) -> int:
        L, R = 0, len(nums) -1

        while nums[L] > nums[R]:
            L += 1
        return nums[L]
