class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        r =[]
        countZeros = nums.count(0)
        if countZeros > 1:
            return [0] * len(nums)

        total = 1
        for n in nums:
            if n == 0:
                continue
            total *= n

        for n in nums:
            if n == 0 and countZeros == 1:
                r.append(total)
            elif countZeros == 1:
                r.append(0)
            else:
                r.append(total//n) 
        
        return r