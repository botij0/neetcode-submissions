class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Worst case the max(piles) if h == len(piles)
        # The other option is to find a number between 1 and max(piles)
        left, right = 1, max(piles)

        possibleSpeeds = []

        if (len(piles) == h):
            return right

        while left <= right:
            middle = (left + right) // 2

            s = self.getSpeed(piles, middle, h)

            if(s != -1):
                possibleSpeeds.append(s)
                right = middle - 1
            else:
                left = middle + 1

        return possibleSpeeds.pop()
    
    def getSpeed(self, piles: List[int], speed:int, hours: int):
        i = 0
        while hours > 0 and i < len(piles):
            banana = piles[i]
            hours -= math.ceil(banana/speed)
            i += 1

        if hours >= 0 and i == len(piles):
            return speed
        else:
            return -1

