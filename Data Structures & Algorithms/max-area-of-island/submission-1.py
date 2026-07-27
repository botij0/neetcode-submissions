class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        R, C = len(grid), len(grid[0])

        result = 0
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 0 or (i,j) in visited:
                    continue
                r = self.dfs(i, j, grid, visited, R, C)
                result = max(result, r)
        
        return result
        

    
    def dfs(self, i: int, j: int, grid:List[List[int]], visited: set, R: int, C: int):
        if min(i, j) < 0 or i >= R or j >= C:
            return 0
        
        if grid[i][j] == 0 or (i,j) in visited:
            return 0

        visited.add((i,j))

        return 1 + (
            self.dfs(i+1, j, grid, visited, R, C) +
            self.dfs(i-1, j, grid, visited, R, C) +
            self.dfs(i, j+1, grid, visited, R, C) +
            self.dfs(i, j-1, grid, visited, R, C)
        )