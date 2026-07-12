class Solution:
    def checkValidString(self, s: str) -> bool:
        left_stack = []
        star_stack = []

        # *)

        for i in range(len(s)):
            if s[i] == '(':
                left_stack.append(i)
            elif s[i] == '*':
                star_stack.append(i)
            else:
                if len(left_stack) <= 0 and len(star_stack) <= 0:
                    return False
                
                if len(left_stack) > 0:
                    left_stack.pop()
                else:
                    star_stack.pop()

        while len(left_stack) > 0:

            if len(star_stack) <= 0:
                return False

            index_star = star_stack.pop()
            index_left = left_stack.pop()

            if index_star < index_left:
                return False

        return True