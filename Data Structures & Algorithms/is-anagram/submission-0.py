class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ds = defaultdict(int)
        dt = defaultdict(int)

        ls = len(s)
        lt = len(t)

        if ls != lt: return False

        for i in range(ls):
            ds[s[i]] += 1
            dt[t[i]] += 1
        
        for i in range(ls):
            if ds[s[i]] != dt[s[i]]: return False
        
        return True