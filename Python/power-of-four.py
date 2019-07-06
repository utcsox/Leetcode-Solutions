class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """

        while num >= 4:
            
            if num % 4 == 0:
                num = num /4
            else:
                return False
        if num == 1:
            return True
        else:
            return False
