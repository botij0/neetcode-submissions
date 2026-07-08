class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        r = []
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)

        while left < right and top < bottom:
            
            # Top Row
            for i in range(left, right):
                r.append(matrix[top][i])
            top +=1

            # Right Row
            for i in range(top, bottom):
                r.append(matrix[i][right - 1])
            right -= 1

            if not(left < right and top < bottom):
                break

            # Bottom Row
            for i in range(right -1, left -1, -1):
                r.append(matrix[bottom - 1][i])
            bottom -=1

            # Left Row
            for i in range(bottom -1, top -1 , -1):
                r.append(matrix[i][left])
            left += 1

        return r

