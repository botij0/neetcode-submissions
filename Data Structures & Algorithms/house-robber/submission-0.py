class Solution:
    def rob(self, nums: List[int]) -> int:
        # [1, 9, 1, 1, 10, 1]
        nums.append(0)
        nums.append(0)
        nums.append(0)
        # [1, 9, 1, 1, 10, 1, 0, 0, 0]

        for i in range(len(nums)-4, -1, -1):
            nums[i] += max(nums[i+2], nums[i+3])

        
        return max(nums)
