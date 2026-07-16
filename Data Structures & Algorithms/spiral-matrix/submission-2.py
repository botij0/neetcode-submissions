class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        L, R = 0, len(matrix[0])
        T, D = 0, len(matrix)
        r= []

        while L < R and T < D:
            # Top Row
            for i in range(L, R):
                r.append(matrix[T][i])
            T += 1

            # Right Row
            for i in range(T, D):
                r.append(matrix[i][R - 1])
            R -= 1

            if not(L < R and T < D):
                break

            # Down Row
            for i in range(R-1, L - 1, -1):
                r.append(matrix[D-1][i])
            D -= 1

            # Left Row
            for i in range(D-1, T - 1, -1):
                r.append(matrix[i][L])
            L += 1
        
        return r