class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        L, R = 0, len(matrix) - 1

        while L < R:
            for i in range(R - L):
                top, bottom = L, R

                # Save the top_left
                top_left = matrix[top][L + i]

                # move bottom left into top left
                matrix[top][L + i] = matrix[bottom - i][L]

                # move bottom right into bottom left
                matrix[bottom - i][L] = matrix[bottom][R - i]

                # move top right into bottom right
                matrix[bottom][R - i] = matrix[top + i][R]

                # move top left into top right
                matrix[top + i][R] = top_left
        
            L += 1
            R -= 1
    
