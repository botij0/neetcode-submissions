class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [n for n in cost] + [0]
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2,len(dp)):
            dp[i] = dp[i] + min(dp[i-1],dp[i-2])
    
        return dp[-1]