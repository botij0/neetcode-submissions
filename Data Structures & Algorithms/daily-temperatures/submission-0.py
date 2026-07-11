class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        LT = len(temperatures)
        stack = [(0, temperatures[0])]
        r = [0] * LT
        for i in range(1,LT):
            if stack[-1][1] >= temperatures[i]:
                stack.append((i, temperatures[i]))
                continue

            while stack and stack[-1][1] < temperatures[i]:
                j, v = stack.pop()
                r[j] = i - j
            
            stack.append((i, temperatures[i]))
           

        return r