class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        visit = set()
        q = deque()

        def addCell(i, j):
            if min(i,j) < 0 or i >= R or j >= C:
                return
            
            if (i,j) in visit or grid[i][j] == 0:
                return

            visit.add((i,j))
            q.append((i,j))


        for i in range(R):
            for j in range(C):
                if grid[i][j] == 2:
                    q.append((i,j))
                    visit.add((i,j))
        
        time = 0
        while q:
            for _ in range(len(q)):
                i, j = q.popleft()
                grid[i][j] = 2

                addCell(i+1, j)
                addCell(i-1, j)
                addCell(i, j+1)
                addCell(i, j-1)

            if q:
                time += 1
        
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 1:
                    return -1

        return time
