class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        r = []
        flag = False
        for i in range(len(digits) -1, -1, -1):
            if not flag and digits[i] != 9:
                digits[i] += 1
                flag = True
            elif not flag:
                digits[i] = 0

            
            r.append(digits[i])

        if not flag:
            r.append(1)

        r.reverse()
        return r