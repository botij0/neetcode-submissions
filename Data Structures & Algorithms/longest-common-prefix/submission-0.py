class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        r = []
        
        for i in range(len(strs[0])):
            r.append(strs[0][i])
            for j in range(1, len(strs)):
                if strs[j][i] != r[-1]:
                    r.pop()
                    return "".join(r)
        
        return strs[0]