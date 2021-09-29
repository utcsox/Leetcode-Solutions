class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        
        tmp = defaultdict(list)
        output = 2**31-1
        
        #1.  Create a dictionary of word and index pair
        for index in range(len(wordsDict)):
            if wordsDict[index] == word1:
                tmp[word1].append(index)
                
            elif wordsDict[index] == word2:
                tmp[word2].append(index)
                
        # find difference of this two list
        
        for p1 in tmp[word1]:
            for p2 in tmp[word2]:
                output = min(output, abs(p1-p2))
                
        return output
