class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        while n != 1 and n not in visited:
            visited.add(n)

            s = str(n)
            n = 0
            for c in s:
                n += int(math.pow(int(c), 2))
        

        return True if n == 1 else False
            