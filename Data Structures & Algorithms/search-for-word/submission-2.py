class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        R, C = len(board), len(board[0])

        for i in range(R):
            for j in range(C):
                if board[i][j] != word[0]:
                    continue

                visited = set()
                if self.dfs(board, word, 0, i, j, visited, R, C):
                    return True

                
        return False

    def dfs(self, board: List[List[str]], word: str, c: int, i:int, j:int, visited: set, R:int, C:int):
        if min(i,j) < 0 or i >= R or j >= C:
            return False
        
        if (i,j) in visited:
            return False
        
        if c >= len(word) or board[i][j] != word[c]:
            return False
        
        if board[i][j] == word[c] and c == len(word) - 1:
            return True

        visited.add((i, j))

        r = (
            self.dfs(board, word, c+1, i+1, j, visited, R, C) or
            self.dfs(board, word, c+1, i-1, j, visited, R, C) or
            self.dfs(board, word, c+1, i, j+1, visited, R, C) or
            self.dfs(board, word, c+1, i, j-1, visited, R, C)
        )

        visited.remove((i,j))
        return r
