class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        L, R = 1, max(piles)
        
        result = R

        while L <= R:
            m = (R + L) // 2

            time = self.helper(piles, m)

            if time <= h:
                result = m
                R = m - 1
            else:
                L = m + 1

        return result
    

    def helper(self, piles: List[int], speed:int) -> int:
        r = 0
        for p in piles:
            r += math.ceil(float(p)/speed)
    
        return r



            
