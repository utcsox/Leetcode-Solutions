class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        from collections import Counter
        lookup = Counter(s)
        for index, char in enumerate(s):
            
            if lookup[char] == 1:
                return index
        return -1
 
 class Solution2(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        lookup = {}
        for char in s:
            if char in lookup:
                lookup[char] += 1
            else:
                lookup[char] = 1
        
        for index, char in enumerate(s):
            
            if lookup[char] == 1:
                return index
        return -1
