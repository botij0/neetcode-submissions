class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        if grid[0][0] == 1 or grid[rows-1][cols-1] == 1:
            return -1 

        visit = set()
        queue = deque()

        visit.add((0,0))
        queue.append((0,0))

        movements = [
            [0, 1],
            [0, -1],
            [1,0],
            [-1,0],
            [1,1],
            [-1,1],
            [1,-1],
            [-1,-1]
        ]

        length = 1
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()

                if r == rows - 1 and c == cols - 1:
                    return length
                
                for dr, dc in movements:
                    new_r, new_c = r + dr, c + dc

                    if(min(new_r, new_c) < 0 or 
                        new_r == rows or new_c == cols or
                        (new_r, new_c) in visit
                        or grid[new_r][new_c] == 1                   
                    ):
                        continue

                    queue.append((new_r, new_c))
                    visit.add((new_r, new_c))
                
            length +=1

        return -1
