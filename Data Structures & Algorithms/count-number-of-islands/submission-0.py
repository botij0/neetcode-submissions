class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        r = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '0':
                    continue
                
                if (i,j) in visited:
                    continue
                
                r += 1
                self.dfs(grid, i, j, visited)
                
        return r

    def dfs(self, grid: List[List[str]], i: int, j: int, visited: set):
        if i < 0 or i>= len(grid) or j >= len(grid[0]) or j < 0:
            return

        if grid[i][j] == '0' or (i,j) in visited:
            return

        visited.add((i,j))
        self.dfs(grid, i+1, j, visited)
        self.dfs(grid, i-1, j, visited)
        self.dfs(grid, i, j + 1, visited)
        self.dfs(grid, i, j-1, visited)