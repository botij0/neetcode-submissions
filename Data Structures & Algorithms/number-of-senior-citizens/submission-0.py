class Solution:
    def countSeniors(self, details: List[str]) -> int:
        result = 0
        for p in details:
            age = int(p[11:13])
            if age > 60:
                result += 1
            
        return result