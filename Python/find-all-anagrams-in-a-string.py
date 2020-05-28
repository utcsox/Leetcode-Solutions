class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result = []
        if len(s) < len(p) == 0:
            return result
        sort_p = ''.join(sorted(p))
        str_len = len(p)
        
        for index in range(len(s) - str_len + 1):
            tmp = s[index:index+str_len]
            tmp = ''.join(sorted(tmp))
            if tmp == sort_p:
                result.append(index)
        return result
