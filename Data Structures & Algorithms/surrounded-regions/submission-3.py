class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return
        
        m, n = len(board), len(board[0])
        
        # Start DFS only from border 'O's to mark connected non-surrounded regions
        for i in range(m):
            self.dfs(board, i, 0)
            self.dfs(board, i, n - 1)

        for j in range(n):
            self.dfs(board, 0, j)
            self.dfs(board, m - 1, j)
            
        # Flip all remaining 'O' to 'X', and restore 'T' back to 'O'
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'

                elif board[i][j] == 'T':
                    board[i][j] = 'O'
                    

    def dfs(self, board: List[List[str]], i: int, j: int):
        if min(i, j) < 0 or i >= len(board) or j >= len(board[0]):
            return
        
        if board[i][j] != 'O':
            return
        
        board[i][j] = 'T'
        
        self.dfs(board, i+1, j)
        self.dfs(board, i-1, j)
        self.dfs(board, i, j+1)
        self.dfs(board, i, j-1)