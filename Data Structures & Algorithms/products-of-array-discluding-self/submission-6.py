class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        preProd = [1]
        postProd = [1]
        current = 1
        for n in nums:
            current *= n
            preProd.append(current)
        
        current = 1
        for i in range(len(nums)-1, -1, -1):
            current *= nums[i]
            postProd.append(current)

        postProd.reverse()

        result = []

        for i in range(len(nums)):
            result.append(preProd[i] * postProd[i+1])

        return result
        