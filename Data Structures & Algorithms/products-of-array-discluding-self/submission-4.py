class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        L = len(nums)
        prefix = [1] * L
        postfix = [1] * L

        for i in range(1, L):
            prefix[i] = nums[i-1] * prefix[i-1]

        for i in range(L-2, -1, -1):
            postfix[i] =  nums[i+1] * postfix[i+1]
        
        r = []
        for i in range(L):
            r.append(prefix[i]*postfix[i])

        return r