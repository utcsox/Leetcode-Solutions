class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        # most frequent task has x number of occurance
        # The idle shall only apply to (x-1) occurance, -> (x-1) * n slot require
        # Adding the most frequent task of (x-1) -> (x-1) * (n+1) slot require
        # Need to add the last element of most frequent tasks
        
        #1.  Create a python Counter
        lookup = collections.Counter(tasks)
        
        #2.  Sort the python counter to find the max occurance  
        sortedlookup = sorted(lookup.values(), reverse=True)
        max_frequency = sortedlookup[0]
        
        #3.  Find # of times the Counter object has max value 
        count = 0
        for index in range(len(sortedlookup)):
            if sortedlookup[index] == max_frequency:
                count += 1
           
        return max(((max_frequency - 1) * (n+1) + count), len(tasks))

    
class Solution2:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        counts = Counter(tasks)
        hq  = [-count for count in counts.values()]
        heapq.heapify(hq)
        
        q, time = deque(), 0
        
        while hq or q:  
            
            time += 1 
            
            if hq:
                count = 1 + heapq.heappop(hq)
                if count:
                    q.append((count, time + n))
                    
            if q and q[0][1] == time:
                heapq.heappush(hq, q.popleft()[0])
            
            
        return time
