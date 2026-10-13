class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        result = []
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                current = [False, False]
                visited = set()
                self.dfs(heights, visited, current, i, j, 1001)

                if current[0] == True and current[1] == True:
                    result.append([i,j])
                    
        return result

    def dfs(self, heights: List[List[int]], visited: set, current: List[bool], i:int, j:int, prev: int):
        if min(i,j) < 0 or i >= len(heights) or j >= len(heights[0]):
            if i < 0 or j < 0:
                current[0] = True
                      
            if i >= len(heights) or j >= len(heights[0]):
                current[1] = True
            
            return

        if current[0] == True and current[1] == True:
            return
        
        if (i,j) in visited or heights[i][j] > prev:
            return
        
        visited.add((i,j))
        
        self.dfs(heights, visited, current, i+1, j, heights[i][j])
        self.dfs(heights, visited, current, i-1, j, heights[i][j])
        self.dfs(heights, visited, current, i, j+1, heights[i][j])
        self.dfs(heights, visited, current, i, j-1, heights[i][j])
        
