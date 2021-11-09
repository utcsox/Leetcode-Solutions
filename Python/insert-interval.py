class Solution1:
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
    
class Solution2:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        output = []
        
        intervals.sort(key = lambda x: x[0])
        
        for index in range(len(intervals)):
            
            #if end value of new interval is smaller than start value of current interval
            if newInterval[1] < intervals[index][0]:
                output.append(newInterval)
                return output + intervals[index:]
            
            # if start value of new interval is larger than end value of current interval
            elif newInterval[0] > intervals[index][1]:
                output.append(intervals[index])
            
            # if there is overlap
            else:
                newInterval = [min(newInterval[0], intervals[index][0]), max(newInterval[1], intervals[index][1])]
                
        output.append(newInterval)
        
        return output
