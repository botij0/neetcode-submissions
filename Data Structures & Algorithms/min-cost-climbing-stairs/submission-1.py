class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # cache = {}
        # r =  min(self.memoization(cost, 0, cache),self.memoization(cost, 1, cache))
        # return r
        return self.dp(cost)
    

    def memoization(self, cost: List[int], i:int, cache:dict):
        if i >= len(cost):
            return 0
        
        if i in cache:
            return cache[i]
        
        cache[i] = cost[i] + min(self.memoization(cost, i+1, cache), self.memoization(cost, i+2, cache))
        return cache[i]
    
    def dp(self, cost: List[int]):
        cost.append(0)
        
        for i in range(len(cost)-3, -1, -1):
            cost[i] += min(cost[i+1],cost[i+2])
        
        return min(cost[0], cost[1])