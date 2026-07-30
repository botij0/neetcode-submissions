class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        result = []
        for i in range(1, rowIndex + 2):
            current = []
            for j in range(i):
                if j == 0 or j == i-1:
                    current.append(1)
                else:
                    current.append(result[i-2][j-1] + result[i-2][j])
            
            result.append(current)
        
        return result[rowIndex]