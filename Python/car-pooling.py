class Solution1:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        timestamp = [0]*1001
        
        for people, start, stop in trips:
            timestamp[start] += people
            timestamp[stop] -= people
            
        used_capacity = 0
        
        for passenger in timestamp:
            used_capacity += passenger
            if used_capacity > capacity:
                return False
            
        return True
      
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
      
        tmp = []
        for people, start, end in trips:
            tmp.append([start, people])
            tmp.append([end, -people])
            
        tmp.sort(key = lambda x: (x[0], x[1]))
        print(tmp)
        
        used_capacity = 0
        
        for pair in tmp:
            used_capacity += pair[1]
            if used_capacity > capacity:
                return False
            
            
        return True
