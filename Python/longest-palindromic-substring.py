class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        output, output_length = '', 0
        
        for index in range(len(s)):
            
            # odd length
            left, right = index, index
            
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right-left+1) > output_length:
                    output = s[left: right + 1]
                    output_length = right-left + 1
                left -= 1
                right += 1
                
            # even length
            left, right = index, index+1
            
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right-left+1) > output_length:
                    output = s[left: right + 1]
                    output_length = right-left + 1
                left -= 1
                right += 1
                
        return output
