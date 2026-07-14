class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t == "+":
                y, x = stack.pop(), stack.pop()
                stack.append(x + y)
            elif t == '-':
                y, x = stack.pop(), stack.pop()
                stack.append(x - y)
            elif t == '*':
                y, x = stack.pop(), stack.pop()
                stack.append(x * y)
            elif t == '/':
                y, x = stack.pop(), stack.pop()
                stack.append(int(x/y))
            else:
                stack.append(int(t))

        print(stack)
        return stack.pop()