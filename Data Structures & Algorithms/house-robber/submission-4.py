class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        L = len(nums)
        if L == 1:
            return nums[0]

        dp = [0] * L
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, L):
            dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])
        
        return dp[-1]

    # 5,1,2,10,6,2,7,9,3,1
    # 5 100 2 10 6 2 7 9 3 1
