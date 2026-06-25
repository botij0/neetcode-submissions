class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = [[]]

        for n in nums:
            next_permutations = []
            for p in permutations:
                for i in range(len(p) + 1):
                    copy = p.copy()
                    copy.insert(i, n)
                    next_permutations.append(copy)
            
            permutations = next_permutations
        
        return permutations