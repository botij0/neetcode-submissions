class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = []
        star_stack = []

        for i in range(len(s)):
            c = s[i]
            if c == '(':
                stack.append(i)
            
            elif c == '*':
                star_stack.append(i)

            else:
                if not stack and not star_stack:
                    return False
              
                elif not stack:
                    star_stack.pop()
                
                else: 
                    stack.pop()

        while star_stack and stack:
            indexStar = star_stack.pop()
            index = stack.pop()

            if index > indexStar:
                return False
                    
        
        return True if len(stack) == 0 else False
            
