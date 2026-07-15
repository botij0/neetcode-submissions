class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cache = [[0] * n for _ in range(m)]
        print(cache)
        return self.memoization(0, 0, m, n, cache)
    
    def memoization(self, i: int, j: int, m: int, n: int, cache: List[List[int]]):
        if i >= m or j >= n:
            return 0

        if cache[i][j] > 0:
            return cache[i][j]
        
        if i == m -1 and j == n - 1:
            return 1
                
        cache[i][j] =  self.memoization(i+1, j, m, n, cache) + self.memoization(i, j+1, m, n, cache)
        return cache[i][j]