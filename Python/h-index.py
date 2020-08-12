class Solution1:
    def hIndex(self, citations: List[int]) -> int:
        
        # sort citations in reverse
        
        citations.sort(reverse=True)
        
        h = 0
        for index in range(len(citations)):
            if citations[index] > index:
                h = index + 1
                
        return h
