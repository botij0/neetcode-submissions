class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        d = defaultdict(list)

        for s in strs:
            aux = [0] * 26
            for c in s:
                aux[ord(c) - ord('a')] += 1

            d[str(aux)].append(s)
        
        for val in d.values():
            result.append(val)
        
        return result
