class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort(key = lambda x: x[0])
        
        result, prevEnd = 0, intervals[0][1]
        
        for start, end in intervals[1:]:
            if start >= prevEnd:
                prevEnd = end
                
            else:
                prevEnd = min(end, prevEnd)
                result += 1
                
        return result
