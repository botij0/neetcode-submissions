class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [(p,s) for p,s in zip(position,speed)]
        pairs.sort()
        stack = []
        r = 0

        for i in range(len(pairs)-1,-1,-1):
            p,s = pairs[i]
            time = (target - p) / s
            stack.append(time)

            if len(stack) > 1 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)