class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        ns = []
        for c in s:
            if c == '#':
                if ns:
                    ns.pop()
                continue
            ns.append(c)
        
        nt = []
        for c in t:
            if c == '#':
                if nt:
                    nt.pop()
                continue
                
            nt.append(c)
        
        return "".join(ns) == "".join(nt)