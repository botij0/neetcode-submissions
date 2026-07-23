class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        L = len(hand)
        if L % groupSize != 0:
            return False

        freq = defaultdict(int)
        hand.sort()

        for n in hand:
            freq[n] += 1
        

        N = L // groupSize
        n = 0

        while n < N:
            lastK = None
            current = []
            for k,v in freq.items():
                if len(current) == groupSize:
                    break

                if v < 1:
                    continue
               
                if lastK and k > lastK + 1:
                    return False

                current.append(k)
                lastK = k
                freq[k] -= 1

            if len(current) < groupSize:
                return False
            
            n += 1

        return True