class Solution:
    def mySqrt(self, x: int) -> int:
        L , R = 1, x//2 + 1

        result = 0
        while L <= R:
            mid = (L+R)//2
            guess = mid * mid

            if guess > x:
                R = mid - 1
            else:
                # result = max(result, mid)
                L = mid + 1
        
        return L - 1
