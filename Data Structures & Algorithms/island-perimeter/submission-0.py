class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    continue
                return self.dfs(grid, visited, i, j)

        return -1

    def dfs(self, grid: List[List[int]], visited: set,  i:int, j:int):
        if min(i,j) < 0 or i >= len(grid) or j>= len(grid[0]):
            return 1
        
        if grid[i][j] == 0:
            return 1

        if (i,j) in visited:
            return 0
        
        visited.add((i,j))

        total = (
            self.dfs(grid, visited, i+1, j) +
            self.dfs(grid, visited, i-1, j) +
            self.dfs(grid, visited, i, j+1) +
            self.dfs(grid, visited, i, j-1)
        )
        return total
