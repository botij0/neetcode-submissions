class Solution:
    def arrangeCoins(self, n: int) -> int:
        return self.binarySearch(n)
    
    def binarySearch(self, n: int):
        # n/2 * (n + 1)
        L, R = 1, n
        stairs = 0
        
        while L <= R:
            mid = (L + R) // 2
            coins = (mid * (mid + 1)) // 2

            if coins > n:
                R = mid -1
            else:
                stairs = max(stairs, mid)
                L = mid + 1

        return stairs
    

    def bruteForce(self, n:int):
        i = 1
        while n > 0:
            n -= i
            i += 1
        
        if n < 0:
            return i - 2
        else:
            return i -1
#
# #
# # #
# # # #
# # # # #