class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        digits = {
            "0": 0,
            "1": 1,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9
        }

        n1 = 0
        L1 = len(num1)
        for i in range(L1 - 1, -1, -1):
            aux = 10**(L1-1-i)
            n1 += digits[num1[i]] * aux

        n2 = 0
        L2 = len(num2)
        for i in range(L2 - 1, -1, -1):
            aux = 10**(L2-1-i)
            n2 += digits[num2[i]] * aux
        
        return str(n1 * n2)