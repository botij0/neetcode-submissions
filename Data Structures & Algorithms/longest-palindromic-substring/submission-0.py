class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = 0
        palindrome = ""

        for i in range(len(s)):
            # Odd length
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > length:
                    length = r - l + 1
                    palindrome = s[l:r+1]
                
                r += 1
                l -= 1
            
            # Even length
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > length:
                    length = r - l + 1
                    palindrome = s[l:r+1]
                
                r += 1
                l -= 1
        
        return palindrome
