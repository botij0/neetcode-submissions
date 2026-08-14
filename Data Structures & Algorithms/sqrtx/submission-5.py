class Solution:
    def mySqrt(self, x: int) -> int:
        L , R = 1, x//2 + 1

        while L <= R:
            mid = (L+R)//2
            guess = mid * mid

            if guess > x:
                R = mid - 1
            else:
                L = mid + 1
        
        return L - 1
