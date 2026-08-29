class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digidict = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }

        result = []
        self.backtraking(digits, result, digidict, [], 0)
        return result
    
    def backtraking(self, digits: str, result: List[str], digidict: dict, current: List[str], i:int):
        if i >= len(digits):
            if current:
                result.append("".join(current))
            return
        
        for c in digidict[digits[i]]:
            current.append(c)
            self.backtraking(digits, result, digidict, current, i + 1)
            current.pop()
        
