class Solution1:
    def findTheDifference(self, s: str, t: str) -> str:
        dict_item = {}

        for char in s:
            if char in dict_item:
                dict_item[char] += 1
            else:
                dict_item[char] = 1
        
        for char in t:
            if char not in dict_item:
                return char
            elif dict_item[char] == 0:
                return char
            else:
                dict_item[char] -= 1
