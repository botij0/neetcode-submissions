class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n_islands = 0
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '0' or (i,j) in visited:
                    continue

                n_islands += 1
                self.bfs(grid, i, j, visited)

        
        return n_islands
    
    def bfs(self, grid: List[List[str]], i:int, j:int, visited: set):
        ROWS, COLS = len(grid), len(grid[0])
        queue = deque()

        queue.append((i,j))
        visited.add((i,j))

        while queue:
            r, c = queue.popleft()
            
            movs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for dr, dc in movs:
                nr = r + dr
                nc = c + dc

                if min(nr, nc) < 0 or nr >= ROWS or nc >= COLS:
                    continue
                
                if (nr, nc) in visited or grid[nr][nc] == '0':
                    continue

                queue.append((nr, nc))
                visited.add((nr, nc))
