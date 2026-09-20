class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count1 = defaultdict(int)
        for c in s1:
            count1[c] += 1
        
        for i in range(len(s2) - (len(s1)-1)):
            if s2[i] in count1 and self.isPermutation(s2[i: i + len(s1)], count1):
                return True
        
        return False
    

    def isPermutation(self, subs: str, count1: dict):
        count2 = defaultdict(int)
        for c in subs:
            count2[c] += 1

        return count1 == count2