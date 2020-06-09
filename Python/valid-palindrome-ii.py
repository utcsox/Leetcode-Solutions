class Solution:
    def validPalindrome(self, s: str) -> bool:
        def helper(s, left, right):
            while left < right:
                if s[left] == s[right]:
                    left, right = left+1, right-1
                else:
                    return False
                
            return True
        left, right = 0, len(s)-1
        while left < right:
            if s[left] == s[right]:
                left, right = left+1, right-1
            else:
                return helper(s, left, right-1) or helper(s, left+1, right)
            
        return True
