class Solution1:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1dict = collections.defaultdict(int)
        for char in s1:
            s1dict[char] += 1
            
        for index in range(len(s2)- len(s1) + 1):
            s2dict = collections.defaultdict(int)
            for char in s2[index:index+len(s1)]:
                s2dict[char] += 1
            if s1dict == s2dict:
                return True
            
        return False
