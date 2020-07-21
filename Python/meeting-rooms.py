class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        
        if len(intervals) <= 1:    
            return True
        
        # 1.  Sort the intervals
        intervals.sort(key= lambda x:x[0])
        
        # 2.  If the end time of previous interval is greater than beg time of current interval -> False

        for i in range(1, len(intervals)):
            if intervals[i-1][1] > intervals[i][0]:
                return False
        
        #3.  If the condition list in #2 never fail, then return True
        return True
