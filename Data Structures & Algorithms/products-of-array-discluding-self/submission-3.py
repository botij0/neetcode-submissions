class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        r = []
        l = len(nums)
        prefix = [1] * (l)
        postfix = [1] * (l)

        pre = 1
        post = 1
        for i in range(l):
            pre *= nums[i]
            post *= nums[l-1-i]

            prefix[i] = pre
            postfix[l-i-1] = post

        for i in range(l):
            if i == 0:
                r.append(1 * postfix[i+1])
            elif i == l - 1:
                r.append(1 * prefix[i-1])
            else:
                r.append(prefix[i-1] * postfix[i+1])
        
        return r