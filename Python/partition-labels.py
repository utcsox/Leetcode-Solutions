class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        output = []
        
        if not S:
            return output
        
        # 1. Create a dictionary that store the last index each character appear
        lookup = {value: key for key, value in enumerate(S)}
        
        # 2.  For subarray, create start and stop of the subarray
    
        first = last = 0
        
        for i, c in enumerate(S):
            
            last = max(last, lookup[c])
            
            if i == last:
                output.append(i - first + 1)
                first = i + 1
            
        
        return output
