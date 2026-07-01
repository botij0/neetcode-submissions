class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 0:
            return []

        r = [[strs[0]]]

        for i in range(1,len(strs)):
            inserted = False
            for l in r:
                aux = l[0]
                if self.isAnagram(aux, strs[i]):
                    l.append(strs[i])
                    inserted = True
                    break
            
            if not inserted:
                r.append([strs[i]])

        return r
    
    def isAnagram(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False

        aux1 = defaultdict(int)
        aux2 = defaultdict(int)

        for i in range(len(s1)):
            aux1[s1[i]] += 1
            aux2[s2[i]] += 1

        for c in s1:
            if aux1[c] != aux2[c]:
                return False

        return True