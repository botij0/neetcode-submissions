class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        stack = []
        self.btrack(stack, result, n, 0, 0)
        return result
    
    def btrack(self, stack: List[str], result: List[str], n:int, openN:int, closedN:int):
        if openN == closedN == n:
            result.append("".join(stack))
        
        if openN > n or closedN > n:
            return
        
        if openN < n:
            stack.append("(")
            self.btrack(stack, result, n, openN+1, closedN)
            stack.pop()
        
        if closedN < openN:
            stack.append(")")
            self.btrack(stack, result, n, openN, closedN+1)
            stack.pop()
    
        
