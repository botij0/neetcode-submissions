class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        L, R = 0, len(s1) - 1

        L2 = len(s2)
        if R + 1 > L2:
            return False

        letters = set(s1)
        
        while R < L2:

            if s2[L] in letters and s2[R] in letters:
                if self.isPermutation(s1, s2[L:R+1]):
                    return True

            L += 1
            R += 1

        return False
    
    def isPermutation(self, s1: str, sub2: str):
        cs1 = Counter(s1)
        cs2 = Counter(sub2)

        for c in s1:
            if cs1[c] != cs2[c]:
                return False
        
        return True