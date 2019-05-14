class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        for i in range(len(strs[0])):
            for j in strs[1:]:
                if i>=len(j) or strs[0][i] != j[i]:
                    return strs[0][0:i]
        return strs[0]
