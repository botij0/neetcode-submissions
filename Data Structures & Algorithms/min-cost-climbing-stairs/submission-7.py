class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # return min(
        #     self.memoization(cost, {}, 0),
        #     self.memoization(cost, {}, 1)
        # )
        return self.dp(cost)

    def dp(self, cost: List[int]):
        n2 = cost[0]
        n1 = cost[1]

        for i in range(2, len(cost)):
            aux = n1
            n1 = cost[i] + min(n1, n2)
            n2 = aux
        
        return min(n1, n2)

    
    def memoization(self, cost: List[int], cache: dict, i: int):
        if i < 0 or i >= len(cost):
            return 0
        
        if i in cache:
            return cache[i]
        
        cache[i] = cost[i] + min(
            self.memoization(cost, cache, i + 1), 
            self.memoization(cost, cache, i+2)
        )

        return cache[i]