class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = [[]]

        for n in nums:
            currPerm = []
            for p in permutations:
                for i in range(len(p) + 1):
                    aux = p.copy()
                    aux.insert(i, n)
                    currPerm.append(aux)

            permutations = currPerm

        return permutations