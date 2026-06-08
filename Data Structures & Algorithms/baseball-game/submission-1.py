class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for o in operations:
            if o == '+':
                b = stack.pop()
                a = stack.pop()
                c = a + b
                stack.append(a)
                stack.append(b)
                stack.append(c)
            elif o == 'C':
                stack.pop()
            elif o == 'D':
                x = stack.pop()
                stack.append(x)
                stack.append(x*2)
            else:
                stack.append(int(o))

        return sum(stack)
