class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cache = [[0] * n for _ in range(m)]
        r, c = 0, 0

        r = self.memoization(r, c, m, n, cache)
        return r
    
    def memoization(self, r: int, c: int, rows: int, cols: int, cache: List[List[int]]):
        if r == rows or c == cols:
            return 0

        if cache[r][c] > 0:
            return cache[r][c]
        
        # Corner
        if r == rows -1 and c == cols - 1:
            return 1
        
        cache[r][c] = (self.memoization(r + 1, c, rows, cols, cache) +
                      self.memoization(r, c + 1, rows, cols, cache))
        
        return cache[r][c]
