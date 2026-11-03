class Solution:
    def minOperations(self, logs: List[str]) -> int:
        result = 0
        for s in logs:
            if s == './':
                continue
            elif s == '../':
                if result == 0:
                    continue
                result -= 1
            else:
                result += 1
        return result