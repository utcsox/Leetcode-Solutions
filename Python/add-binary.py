class Solution1:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a,2) + int(b,2))[2:]

class Solution2:
    def addBinary(self, a: str, b: str) -> str:
        first = len(a)-1
        second = len(b)-1

        carry, total, result = 0, 0, ''
        while (first >= 0 or second >=0):
            total = carry
            if first >= 0:
                total = total + int(a[first])
            if second >= 0:
                total = total + int(b[second])
            result = result + str(total%2)
            carry = int(total/2)
            first = first-1
            second = second -1
        if carry != 0: 
            result = result + str(carry)
        return result[::-1]
    
class Solution3:
    def addBinary(self, a: str, b: str) -> str:
        
        # answer is equal to sum of two binary + carry
        x, y = int(a, 2), int(b, 2)
        
        # (x^y) -> ^ exclusive or is sum of two binary
        # (x&y) << 1 the carry bit is 1 if both binary are 1.  shift to the left by 1
        while y:
            x, y = x^y , (x&y)<<1
            
        return bin(x)[2:]
