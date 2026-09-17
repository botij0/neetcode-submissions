class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)

        for s in strs:
            aux = [0] * 26
            for c in s:
                aux[ord(c) - ord('a')] += 1

            d[str(aux)].append(s)
        
        return list(d.values())
