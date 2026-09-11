class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = {}
        return min(self.memoization(cost, cache, 0), self.memoization(cost, cache, 1))

    def memoization(self, cost: List[int], cache: dict, i:int):
        if i  >= len(cost):
            return 0

        if i in cache:
            return cache[i]
        
        cache[i] = cost[i] + min(self.memoization(cost, cache, i+1), self.memoization(cost, cache, i + 2))
        return cache[i]