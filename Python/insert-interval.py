class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        output = []
        
        intervals.sort(key = lambda x: x[0])
        
        # 1.  add all intervals start before newInterval
        for start, end in intervals: 
            if start < newInterval[0]:
                output.append([start, end])
                
        if not output or output[-1][1] < newInterval[0]:
            output.append(newInterval)
            
        else:
            output[-1][1] = max(output[-1][1], newInterval[1])
        
        for start, end in intervals:
            if output[-1][1] < start:
                output.append([start,end])
            else:
                output[-1][1] = max(output[-1][1], end)
        
        return output
