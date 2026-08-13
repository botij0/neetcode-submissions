class Solution:
    def validPalindrome(self, s: str) -> bool:
        L, R = 0, len(s) - 1

        while L < R:
            if s[L] != s[R]:
                return self.aux(s[L:R]) or self.aux(s[L+1:R+1])
            
            L += 1
            R -= 1
        
        return True
    
    def aux(self, s: str):
        L, R = 0, len(s) - 1

        while L < R:
            if s[L] != s[R]:
                return False
            
            L += 1
            R -= 1
        
        return True