class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        chars = defaultdict(int)
        result = 1

        L = 0
        maxf = 0

        for R in range(len(s)):
            chars[s[R]] += 1        
            maxf = max(maxf, chars[s[R]])

            while (R - L + 1) - maxf > k:
                chars[s[L]] -= 1
                L += 1
              
            result = max(result, R - L + 1)
        
        return result
        

        