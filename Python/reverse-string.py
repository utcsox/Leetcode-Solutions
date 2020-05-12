class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        
        s.reverse()
        
class Solution2(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        
        for i in range(len(s)//2):
            s[i], s[-i-1] = s[-i-1], s[i]
            
class Solution3:
def reverseString(self, s: List[str]) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    def helper(start, end, ls):
        if start >= end:
            return
        else:
            ls[start], ls[end] = ls[end], ls[start]

        return helper(start+1, end-1, ls)

    helper(0, len(s)-1, s)     
