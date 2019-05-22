class Solution:
    def isValid(self, s: str) -> bool:
        lookup = {'{': '}', '(': ')', '[': ']'}
        L = []
    
        for char in s:
            if char in lookup:
                L.append(char)
            elif len(L) == 0 or lookup[L.pop()] != char:
                return False
        return len(L) == 0
