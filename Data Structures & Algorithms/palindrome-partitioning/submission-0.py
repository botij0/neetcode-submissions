class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        self.backtracking(s, result, [], 0)
        return result
    
    def backtracking(self, s: str, result: List[List[str]], current: List[str], i:int):
        if i >= len(s):
            result.append(current.copy())
            return
        
        for j in range(i, len(s)):
            if self.isPalindrome(s, i, j):
                current.append(s[i:j+1])
                self.backtracking(s, result, current, j+1)
                current.pop()
        
    
    def isPalindrome(self, s:str, L: int, R:int):
        while L < R:
            if s[L] != s[R]:
                return False
            L += 1
            R -= 1
        return True 