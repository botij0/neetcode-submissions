class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        LW = len(words)
        colWords = [""] * len(words)
        for i in range(LW):
            for j in range(len(words[i])):
                if len(words[i]) > LW:
                    return False
                    
                colWords[j] += words[i][j]
        
        for i in range(LW):
            if words[i] != colWords[i]:
                return False

        return True