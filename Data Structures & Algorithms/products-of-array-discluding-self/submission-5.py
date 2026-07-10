class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        L = len(nums)
        prefix = [nums[0]] * L
        postfix = [nums[L-1]] * L

        for i in range(1, L):
            prefix[i] = nums[i] * prefix[i-1]
        
        for i in range(L-2,-1,-1):
            postfix[i] = nums[i] * postfix[i+1]
        
        postfix.append(1)
        prefix.insert(0,1)

        r = []
        for i in range(1,L+1):
            r.append(prefix[i-1] * postfix[i])

        return r