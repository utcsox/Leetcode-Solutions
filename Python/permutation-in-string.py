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
    
    
class Solution2:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1dict = collections.defaultdict(int)
        for char in s1:
            s1dict[char] += 1

        s2dict = collections.defaultdict(int)
        for char in s2[:len(s1)]:
            s2dict[char] += 1
        #print(s1dict, s2dict)
        if s1dict == s2dict:
            return True

        for index in range(len(s1), len(s2)):
            prev_char = s2[index-len(s1)]
            s2dict[prev_char] -= 1   
            if s2dict[prev_char] < 1:
                s2dict.pop(prev_char)
            s2dict[s2[index]] += 1
            if s1dict == s2dict:
                return True
            #print(index, s2dict)

        return False
