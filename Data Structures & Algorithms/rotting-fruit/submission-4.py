class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        visited = set()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i,j))
        
        time = 0
        while queue:
            for _ in range(len(queue)):
                i,j = queue.popleft()
                grid[i][j] = 2
                self.addCell(grid, visited, queue, i+1, j)
                self.addCell(grid, visited, queue, i-1, j)
                self.addCell(grid, visited, queue, i, j+1)
                self.addCell(grid, visited, queue, i, j-1)
                
            if queue:
                time += 1
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1
        
        return time

    
    def addCell(self, grid: List[List[int]], visited: set, queue: deque, i: int, j: int):
        if min(i,j) < 0 or i >= len(grid) or j >= len(grid[0]):
            return
        
        if (i,j) in visited or grid[i][j] != 1:
            return
        
        queue.append((i,j))
        visited.add((i,j))