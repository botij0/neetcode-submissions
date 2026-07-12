class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        r =0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    continue
                before = len(visited)
                self.dfs(grid, i, j, visited)
                after = len(visited)

                if r < (after - before):
                    r = after - before

        
        return r
    
    def dfs(self, grid: List[List[int]], i:int, j:int, visited:set):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
            return
        
        if grid[i][j] == 0 or (i,j) in visited:
            return

        visited.add((i,j))

        self.dfs(grid, i+1, j, visited)
        self.dfs(grid, i-1, j, visited)
        self.dfs(grid, i, j+1, visited)
        self.dfs(grid, i, j-1, visited)