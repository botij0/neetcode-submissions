class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if t == '+':
                y, x = stack.pop(), stack.pop()
                stack.append(x + y)
            elif t == '*':
                y, x = stack.pop(), stack.pop()
                stack.append(x * y)

            elif t == '-':
                y, x = stack.pop(), stack.pop()
                stack.append(x - y)

            elif t == '/':
                y, x = stack.pop(), stack.pop()
                stack.append(int(float(x)/ y))
            else:
                stack.append(int(t))
        
        return round(stack.pop())