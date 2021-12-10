class Solution1:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) == 0:
            return 0
        
        
        max_length = 0
        
        for i in range(len(s)):
            tempstr = '' + s[i]
            length = 1
            
            for j in range(len(s))[i+1:]:
                
                if s[j] not in tempstr:
                    tempstr += s[j]
                    length += 1
                else:
                    if length > max_length:
                        max_length = length

                    break
            if length >= max_length:
                max_length = length
                    
        return max_length
        
class Solution2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if len(s) <= 1:
            return len(s)
        
        slow, fast = 0, 0
        max_length = 0
        hashset = set()
        
        while fast < len(s) and slow < len(s):
            if s[fast] not in hashset:
                hashset.add(s[fast])
                max_length = max(max_length, len(hashset))
                fast += 1
                
            else:
                hashset.remove(s[slow])
                slow += 1
                
        return max_length   
    
class Solution3:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        if len(s) == 0:
            return 0
        tempstr = ''
        maxLen = 0
        
        for char in s:
            if char not in tempstr:
                tempstr +=  char
                if len(tempstr) > maxLen:
                    maxLen = len(tempstr)
            else: 
                tempstr = tempstr[tempstr.index(char) + 1 : ] + char
            
        return maxLen
    
class Solution4:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        left, output, charSet = 0, 0, set()
        
        for right in range(0, len(s)):
            while s[right] in charSet:
                charSet.remove(s[left])
                left += 1
            charSet.add(s[right])
            
            output = max(output, len(charSet))
            
        return output
                
        
