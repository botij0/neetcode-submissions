class Solution:
    def isPalindrome(self, s: str) -> bool:
        L, R = 0, len(s)-1

        while L < R:

            cl = s[L].lower()
            cr = s[R].lower()


            if cl.isalnum() == False:
                L += 1
                continue
            
            if cr.isalnum() == False:
                R -= 1
                continue

            
            if s[L].lower() != s[R].lower():
                return False

            L += 1
            R -= 1


        return True