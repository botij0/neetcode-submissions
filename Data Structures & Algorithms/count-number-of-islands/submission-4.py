class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        result = 0
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '0' or (i,j) in visited:
                    continue
                
                self.dfs(grid, visited, i, j)
                result += 1
        
        return result
    
    def dfs(self, grid: List[List[str]], visited: set, i: int, j: int):
        if min(i,j) < 0 or i >= len(grid) or j >= len(grid[0]):
            return
        
        if (i,j) in visited or grid[i][j] == '0':
            return
        
        visited.add((i,j))

        self.dfs(grid, visited, i+1, j)
        self.dfs(grid, visited, i-1, j)
        self.dfs(grid, visited, i, j+1)
        self.dfs(grid, visited, i, j-1)