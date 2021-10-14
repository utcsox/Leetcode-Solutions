class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        magazine_dict = defaultdict(int)
        
        for char in magazine:
            if char in magazine:
                magazine_dict[char] += 1
            else:    
                magazine_dict[char] = 1
            
        for char in ransomNote:
            if magazine_dict[char] > 0:
                magazine_dict[char] -= 1
            else:    
                return False
        
        return True
