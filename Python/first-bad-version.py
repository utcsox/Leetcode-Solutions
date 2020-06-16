class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        i, j = 0, n
        
        while i < j:
            midpoint = (i + j )//2
            if not isBadVersion(midpoint):
                i = midpoint + 1
            else:
                j = midpoint
            
        return i
