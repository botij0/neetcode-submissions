class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d = {}
        for i in range(len(t)):           
            if s[i] in d and d[s[i]] != t[i]:
                return False
            if s[i] not in d and t[i] in d.values():
                return False
            d[s[i]] = t[i]

        return True 