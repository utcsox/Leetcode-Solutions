class Solution:
    def reverse(self, x: int) -> int:
        b = 0 
        if x < 0:
            x = abs(x)
            b = 1

        x = str(x)
        l1 = [i for i in x]
        l1.reverse()
        L1=''.join(l1)
        L1 = int(L1)
        L1= L1*(-1) if b == 1 else L1   
        L1 = 0 if abs((L1)) > 0x7FFFFFFF else (L1)
        return  (L1)
