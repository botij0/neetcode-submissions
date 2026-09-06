class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        result = []
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                current = [False, False]
                visited = set()
                self.dfs(heights, visited, current, i, j, 1001)
                if current[0] and current[1]:
                    result.append([i,j])

        return result
    
    def dfs(self, heights: List[List[int]], visited: set, current: list, i:int, j:int, last: int):
        if min(i,j) < 0 or i >= len(heights) or j >= len(heights[0]):
            if i < 0 or j < 0:
                current[0] = True
            else:
                current[1] = True
                
            return
       
        if heights[i][j] > last or (i,j) in visited:
            return
        
        visited.add((i,j))

        self.dfs(heights, visited, current, i+1, j, heights[i][j])
        self.dfs(heights, visited, current, i-1, j, heights[i][j]) 
        self.dfs(heights, visited, current, i, j+1, heights[i][j])
        self.dfs(heights, visited, current, i, j-1, heights[i][j])
