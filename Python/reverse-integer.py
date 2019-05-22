class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        xx = str(abs(x))
        l1 = [i for i in xx][::-1]
        L1 = int(''.join(l1))
        if abs(L1) > 0x7FFFFFFF:
            L1 = 0
        elif x <0:
            L1 = -L1

        return L1
