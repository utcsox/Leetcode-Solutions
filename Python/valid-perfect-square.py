class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        """
        :type num: int
        :rtype: bool
        """
        i,j=0,num
        if num == 1:
            return True
        #mid = num//2
        
        while i<=j:
            mid = (i+j)//2
            if (num/mid) == mid:
                return True
            elif (num/mid)>mid:
                i=mid+1
            else:
                j=mid-1
        return False
