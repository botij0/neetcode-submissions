class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        print(candidates)
        self.btrack(candidates, result, target, 0, [])
        return result

    def btrack(self, candidates: List[int], result: List[List[int]], target: int,  i: int, current: List[int]):
        if target == 0:
            result.append(current.copy())
            return
        
        if i >= len(candidates) or target < 0:
            return

        currval = candidates[i]               
        current.append(currval)
        self.btrack(candidates, result, target - currval, i + 1, current)
        current.pop()
        
        while  i < len(candidates) and candidates[i] == currval:
            i += 1
            
        self.btrack(candidates, result, target, i, current)