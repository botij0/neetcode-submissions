class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # cache = {}
        # return min(self.memoization(cost, cache, 0), self.memoization(cost, cache, 1))
        return self.dp(cost)
    
    def dp(self, cost: List[int]):
        current_step = cost[1]
        previous_step = cost[0]

        for i in range(2, len(cost)):
            temp = current_step
            current_step = cost[i] + min(current_step, previous_step)
            previous_step = temp
        
        return min(current_step, previous_step)


    def memoization(self, cost: List[int], cache: dict, i:int):
        if i  >= len(cost):
            return 0

        if i in cache:
            return cache[i]
        
        cache[i] = cost[i] + min(self.memoization(cost, cache, i+1), self.memoization(cost, cache, i + 2))
        return cache[i]