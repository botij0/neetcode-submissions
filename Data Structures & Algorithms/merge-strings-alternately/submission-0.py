class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        j = 0
        result = ""
        while i < len(word1) and j < len(word2):
            if i <= j:
                result += word1[i]
                i += 1
            else:
                result += word2[j]
                j += 1
        
        result += word1[i:]
        result += word2[j:]
        
        return result