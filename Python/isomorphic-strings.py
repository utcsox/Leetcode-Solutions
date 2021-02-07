class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        lookup = {}
        for i in range(len(s)): 
            
            if s[i] not in lookup:
                if t[i] in lookup.values():
                    return False
                else:
                    lookup[s[i]] = t[i]
            else:
                
                if lookup[s[i]] != t[i]:
                    return False
                
        return True
