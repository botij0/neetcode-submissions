class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            return -1
        
        if haystack == needle:
            return 0

        result = -1
        for i in range(len(haystack)):
            if haystack[i] != needle[0]:
                continue
            
            R = len(needle) + i
            if R <= len(haystack) and haystack[i:R] == needle:
                result = i
                break
        
        return result
