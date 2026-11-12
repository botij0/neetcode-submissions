class Solution:
    def addBinary(self, a: str, b: str) -> str:
        r = []
        carry = 0
        a, b = a[::-1], b[::-1]

        for i in range(max(len(a),len(b))):
            x = a[i] if i < len(a) else "0"
            y = b[i] if i < len(b) else "0"

            if x == '0' and y == '0':
                if carry:
                    r.append("1")
                    carry = 0
                else:
                    r.append("0")
            
            elif (x == '1' and y == '0') or (x == '0' and y == '1'):
                if carry:
                    r.append("0")
                else:
                    r.append("1")
            else:
                if carry:
                    r.append("1")
                else:
                    r.append("0")
                    carry = 1

        if carry:
            r.append("1")
        
        r.reverse()
        return "".join(r)