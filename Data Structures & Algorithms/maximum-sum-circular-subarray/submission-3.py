class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        gMax = nums[0]
        gMin = nums[0]

        currMax = 0
        currMin = 0

        total = 0

        for n in nums:
            currMax = max(currMax + n, n)
            currMin = min(currMin + n, n)

            total += n

            gMax = max(currMax, gMax)
            gMin = min(currMin, gMin)

        return max(gMax, total - gMin) if gMax > 0 else gMax

