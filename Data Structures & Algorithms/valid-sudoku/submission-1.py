class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        columns = defaultdict(list)
        cuadrants = defaultdict(list)

        for i in range(len(board)):
            s_row = set()
            for j in range(len(board[0])):
                c = board[i][j]

                if c == ".":
                    continue

                if c in s_row:
                    return False
                s_row.add(c)

                if c in columns[j]:
                    return False
                columns[j] += c

                if c in cuadrants[(i//3, j//3)]:
                    return False
                cuadrants[(i//3, j//3)] += c
        
 
        return True
