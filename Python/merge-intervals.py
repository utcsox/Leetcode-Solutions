class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # One can merge two element together if the beginning of the second element is smaller than the 
        # end of the first element
        # 1.  sort the array by its first element
        # 2.  To merge overlap interval:
        # 3.  i) if there is no overlap between the previous/current array, add the current array to output
        # 4.  ii) if there is overlap, the last interval end element is equal to   or curent end element)
        
        result = []
        if not intervals:
            return result
        
        intervals.sort(key = lambda x: x[0])
        result.append(intervals[0])
        
        for index in range(1, len(intervals)):
            
            # if no overlap
            if result[-1][1] < intervals[index][0]:
                result.append(intervals[index])
            else:
                result[-1][1] = max(intervals[index][1], result[-1][1])
        
        return result
