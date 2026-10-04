class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        self.btrack(result, s, 0, [])
        return result

    def btrack(self, result: List[List[str]], s: str, i: int, current: List[str]):
        if i >= len(s):
            result.append(current.copy())
            return
        
        for j in range(i, len(s)):
            if self.isPalindrome(s, i, j):
                current.append(s[i:j+1])
                self.btrack(result, s, j+1, current)
                current.pop()
        
    
    def isPalindrome(self, s:str, L: int, R:int):
        while L < R:
            if s[L] != s[R]:
                return False
            L += 1
            R -= 1
        return True 