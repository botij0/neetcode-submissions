class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        r = 0
        for o in operations:
            if o == '+':
                b = stack.pop()
                a = stack.pop()
                c = a + b
                stack.append(a)
                stack.append(b)
                stack.append(c)
                r += c
            elif o == 'C':
                x = stack.pop()
                r -= x
            elif o == 'D':
                x = stack.pop()
                stack.append(x)
                stack.append(x*2)
                r += x*2
            else:
                x = int(o)
                stack.append(x)
                r += x

        return r
