class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        results = []

        intervals.sort(key = lambda x: x[0])
        
        for interval in intervals:
            # if the output is empty, add the first element in there
            if not results:
                results.append(interval)
            # if no overlap
            
            elif results[-1][1] < interval[0]:
                results.append(interval)
                
            # if overlap
            else:
                results[-1][1] = max(results[-1][1], interval[1])
                
        return results
