class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        L, R = 1, max(piles)
        length = len(piles)
        result = R

        while L <= R:
            midSpeed = (L + R) // 2
            time = self.getTime(piles, midSpeed)

            if time <= h:
                result = midSpeed
                R = midSpeed - 1
            else:
                L = midSpeed + 1

        return result
    

    def getTime(self, piles: List[int], speed: int) -> int:
        time = 0
        for p in piles:
            time += math.ceil(p/speed)
            
        return time