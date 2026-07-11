class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        LS = len(s)
        if LS == 0:
            return True
            
        target = s[i]
        for c in t:

            if c == target:
                i += 1
                if i < len(s):
                    target = s[i]
                else:
                    return True
        return False