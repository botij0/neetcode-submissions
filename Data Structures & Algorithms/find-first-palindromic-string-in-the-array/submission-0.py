class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        result = ""
        for w in words:
            if self.isPal(w):
                result = w
                break

        return result
    
    def isPal(self, w: str):
        L, R = 0, len(w)-1

        while L < R:
            if w[L] != w[R]:
                return False

            L += 1
            R -= 1

        return True 
