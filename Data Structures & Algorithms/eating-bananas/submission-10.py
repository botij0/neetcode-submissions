class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        L, R = 1, max(piles)
        result = R
        while L <= R:
            mid = (L + R) // 2
            time = self.aux(piles, mid)

           
            if time <= h:
                R = mid - 1
                result = min(result, mid)
            else:
                L = mid + 1
        
        return result
    
    def aux(self, piles: List[int], speed: int):
        time = 0
        for p in piles:
            time += math.ceil(p / speed)
        
        return time