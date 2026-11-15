class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        aux = num[-1]
        for i in range(len(num)-2, -1,-1):
            aux += num[i] * (10 ** (len(num)-1-i))

        aux = aux + k
        result = []
        i = 1
        while aux > 0:
            
            result.append(aux % (10**i))
            aux = aux // (10**i)

        result.reverse()
        return result