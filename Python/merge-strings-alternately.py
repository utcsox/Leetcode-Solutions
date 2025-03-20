class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word1_pt, word2_pt, output = 0, 0, ""

        while word1_pt < len(word1) and word2_pt < len(word2):

            output += word1[word1_pt]
            word1_pt += 1
            output += word2[word2_pt]
            word2_pt += 1

        output += word1[word1_pt:]
        output += word2[word2_pt:]

        return output
