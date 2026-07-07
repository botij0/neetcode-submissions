class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        ROWS = len(words)      
        for i in range(ROWS):
            col_word = ""
            for j in range(len(words[i])):
                if j >= ROWS or i >= len(words[j]):
                    return False

                col_word += words[j][i]
            
            if col_word != words[i]:
                return False
        
        return True