class Solution:
    def isPalindrome1(self, s: str) -> bool:
        # two-pointer approach
        # 1.  convert the string to lower case
        # 2.  Setup two pointers: one from beg and one from end
        # 3.  if both pointer meet, then it is a palindrome
        string = s.lower()
        beg, end = 0, len(string)-1
        while beg < end:
            if s[beg].isalnum() == False:
                beg += 1
            
            elif s[end].isalnum() == False:
                end -= 1
            
            elif string[beg] != string[end]:
                return False
            else:
                beg = beg +1
                end = end -1
        return True
    
class Solution2:
    def isPalindrome(self, s: str) -> bool:
        
        # a string is a palindrome if itself and its reverse are the same 
        # 1.  convert the string to lower case
        # 2.  add all alpha numeric element into a new string
        # 3.  verify the string is equal to its reverse  
        
        new_s = ''
        s = s.lower()
        for char in s:
            if char.isalnum():
                new_s += char
        return new_s ==  new_s[::-1]
