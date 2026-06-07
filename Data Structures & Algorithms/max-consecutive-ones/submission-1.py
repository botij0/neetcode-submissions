class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        current = 0
        r = 0
        for n in nums:
            if n == 1:
                current +=1
            else:
                if current > r:
                    r = current
                current = 0

        if current > r:
            r = current
        
        return r