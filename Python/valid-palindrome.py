class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = s.lower()
        beg, end = 0, len(string)-1
        while beg < end:
            print(beg, end)
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
