class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefixSum = []
        currentPreSum = 0
        n = len(nums)

        for i in range(n):
            currentPreSum += nums[i]
            prefixSum.append(currentPreSum)

        for i in range(n):
            if i!= 0 and prefixSum[i-1] == prefixSum[n-1] - prefixSum[i]:
                return i
            elif i==0 and prefixSum[n-1] - prefixSum[i] == 0:
                return i
        return -1