class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combinations = []
        self.helper(1, [], combinations, n, k)
        return combinations
    
    def helper(self, i:int, current_comb: List[int], 
        combinations: List[List[int]], n: int, k: int):

        if len(current_comb) == k:
            combinations.append(current_comb.copy())
            return
        
        if i > n:
            return
        
        for j in range(i, n + 1):
            current_comb.append(j)
            self.helper(j + 1, current_comb, combinations, n, k)
            current_comb.pop()
