class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        if not intervals:
            return min_meeting_rooms
        
        # 1.  Sort the intervals list by start time
        intervals.sort(key = lambda x: x[0])
        
        # 2.  Add the first meeting's ending time to the heap
        free_rooms = []
        heapq.heappush(free_rooms, intervals[0][1])
        
        
        # 3.  Check whether the top of queue is free or not
        #   a) if the first element of priority queue < start time of new interval, pop the 
        #.     first element of the priority queue
        #.  b) add the new interval end time to the priority queue
        
        for index in range(1, len(intervals)):
            if free_rooms[0] <= intervals[index][0]:
                heapq.heappop(free_rooms)
                
            heapq.heappush(free_rooms, intervals[index][1])
            
        # 4.  Return the length of priority queue    
        return len(free_rooms)
            
