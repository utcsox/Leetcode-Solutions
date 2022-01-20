class Solution:
    def countSubstrings(self, s: str) -> int:
        
        result = 0
        for index in range(len(s)):
            #even
            left, right = index, index
            
            while left >=0 and right <len(s) and s[left]==s[right]:
                result += 1
                left -= 1
                right += 1
            
            #odd
            left, right = index, index + 1
            while left >=0 and right <len(s) and s[left]==s[right]:
                result += 1
                left -= 1
                right += 1
                
        return result
