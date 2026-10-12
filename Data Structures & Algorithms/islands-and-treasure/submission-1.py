class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue = deque()
        visited = set()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    queue.append((i,j))
                    visited.add((i,j))
        
        distance = 0
        while queue:
            for _ in range(len(queue)):
                i,j = queue.popleft()
                grid[i][j] = distance

                self.addCell(grid, visited, queue, i+1, j)
                self.addCell(grid, visited, queue, i-1, j)
                self.addCell(grid, visited, queue, i, j+1)
                self.addCell(grid, visited, queue, i, j-1)
                
            distance += 1
    
    def addCell(self, grid: List[List[int]], visited: set, queue: deque, i: int, j:int):
        if min(i,j) < 0 or i >= len(grid) or j >= len(grid[0]):
            return
        
        if grid[i][j] == -1 or (i,j) in visited:
            return
        
        visited.add((i,j))
        queue.append((i,j))

        
