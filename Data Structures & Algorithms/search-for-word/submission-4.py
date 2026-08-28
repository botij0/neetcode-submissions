class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != word[0]:
                    continue

                visited = set()           
                if self.dfs(board, word, visited, i, j, 0):
                    return True

        return False
    

    def dfs(self, board: List[List[str]], word: str, visited: set, i:int, j:int, k: int):
        if min(i,j) < 0 or i >= len(board) or j >= len(board[0]):
            return False
        
        if (i,j) in visited or board[i][j] != word[k]:
            return False
        
        if k == len(word) - 1:
            return True

        visited.add((i,j))
        r = (
            self.dfs(board, word, visited, i + 1, j, k+1) or
            self.dfs(board, word, visited, i - 1, j, k+1) or
            self.dfs(board, word, visited, i, j + 1, k+1) or
            self.dfs(board, word, visited, i, j - 1, k+1)
        )

        visited.remove((i,j))
        return r