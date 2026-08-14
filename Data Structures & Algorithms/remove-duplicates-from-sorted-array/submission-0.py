class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        L = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[L] = nums[i]
                L += 1


        return L