class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        aux = {
            ')': '(',
            '}': '{',
            ']': '[' 
        }

        for c in s:
            if c not in aux:
                stack.append(c)
            elif len(stack) > 0:
                op = stack.pop()
                if aux[c] != op:
                    return False
            else:
                return False
        
        return True if len(stack) == 0 else False