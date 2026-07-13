class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        while n != 1 and n not in visited:
            visited.add(n)

            aux = 0
            while n > 0:
                aux += int(math.pow(n%10, 2))
                n = n // 10
            n = aux

        return True if n == 1 else False
            