class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return n
        if n == 1 or n == 2:
            return 1
            
        Tn3, Tn2, Tn1 = 0, 1, 1
        for i in range(2,n):
            aux = Tn1
            Tn1 = Tn3 + Tn2 + Tn1
            Tn3 = Tn2
            Tn2 = aux
        
        return Tn1