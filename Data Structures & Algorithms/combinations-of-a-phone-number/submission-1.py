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
        self.btrack(digits, digidict, result, 0, [])
        return result
    
    def btrack(self, digits: str, digidict: dict, result: List[str], i:int, current: List[str]):
        if i >= len(digits):
            if current:
                result.append("".join(current))
            return
        
        for letter in digidict[digits[i]]:
            current.append(letter)
            self.btrack(digits, digidict, result, i + 1, current)
            current.pop()
        
        
