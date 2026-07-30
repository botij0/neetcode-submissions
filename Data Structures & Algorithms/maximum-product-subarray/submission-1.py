class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = max(nums)
        currMin, currMax = 1, 1

        for n in nums:
            if n == 0:
                currMin, currMax = 1, 1
                continue

            aux = currMax
            currMax = max(n * currMax, n * currMin, n)
            currMin = min(n * currMin, n * aux, n)
            result = max(result, currMax)


        return result