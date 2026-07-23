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

        while stack and star_stack and stack[-1] < star_stack[-1]:
            stack.pop()
            star_stack.pop()
                    
        
        return True if len(stack) == 0 else False
            
