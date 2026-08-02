class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        R, C = len(grid), len(grid[0])
        visited = set()
        r = 0
        for i in range(R):
            for j in range(C):
                if grid[i][j] == "1" and (i,j) not in visited:
                    r += 1
                    self.bfs(grid, i , j, visited, R, C)
        return r
    
    def bfs(self, grid: List[List[str]], i:int, j:int, visited:set, R:int, C:int):
        queue = deque()
        queue.append((i,j))

        while queue:
            xi, xj = queue.popleft()

            if min(xi, xj) < 0 or xi >= R or xj >= C:
                continue
            
            if grid[xi][xj] == "0" or (xi,xj) in visited:
                continue
            
            visited.add((xi, xj))
            
            neighbors = [(0,1), (0,-1), (1,0), (-1,0)]
            for n in neighbors:
                ni, nj = n
                queue.append((xi + ni, xj + nj))
            
