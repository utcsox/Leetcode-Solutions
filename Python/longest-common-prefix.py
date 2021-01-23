class Solution1:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        for i in range(len(strs[0])):
            for j in strs[1:]:
                if i>=len(j) or strs[0][i] != j[i]:
                    return strs[0][0:i]
        return strs[0]

    
 class Solution2:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if not strs:
            return ''
        
        if len(strs) == 1:
            return strs[0]
        
        max_len = max([len(str) for str in strs])
        min_len = min([len(str) for str in strs])
        
        output = ''
        for i in range(max_len):
            if i < min_len:
                tmp = [1 if str[i] == strs[0][i] else 0 for str in strs]
                if all(tmp):
                    output += strs[0][i]
                
                else:
                    return output
            else:
                return output
            
        return output
