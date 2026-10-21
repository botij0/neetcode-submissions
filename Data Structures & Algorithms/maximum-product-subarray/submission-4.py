class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currMax = 1
        currMin = 1
        result = max(nums)

        for n in nums:
            if n == 0:
                currMax = 1
                currMin = 1
                continue
            
            aux = currMax
            currMax = max(currMax * n, currMin * n, n)
            currMin = min(aux * n, currMin * n, n)

            result = max(currMax, result)
        
        return result