class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # cache = [[0] * n for _ in range(m)]
        # r, c = 0, 0

        # r = self.memoization(r, c, m, n, cache)
        # return r
        return self.dp(m,n)
    
    def dp(self, rows: int, cols: int):
        prev_row = [0] * cols

        for r in range(rows - 1, -1, -1):
            current_row = [0] * cols
            current_row[cols-1] = 1

            for c in range(cols-2, -1, -1):
                current_row[c] = current_row[c+1] + prev_row[c]
            
            prev_row = current_row

        return prev_row[0]
    
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
