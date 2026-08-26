class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()

        self.dfs(candidates, result, target, 0, [], 0)
        return result

    
    def dfs(self, candidates: List[int], result: List[List[int]], target: int, i: int, current: List[int], total: int):

        if total == target:
            result.append(current.copy())
            return

        if i >= len(candidates) or total > target:
            return 

        current.append(candidates[i])
        self.dfs(candidates, result, target, i+1, current, total + candidates[i])
        current.pop()

        # skip same values
        while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
            i += 1

        self.dfs(candidates, result, target, i+1, current, total)
        
