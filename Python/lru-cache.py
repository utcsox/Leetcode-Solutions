class LRUCache:

    def __init__(self, capacity: int):
        
        # define a dequeue to track the order of key
        # define a dictionary to track key/value
        self.capacity = capacity
        self.order = deque()
        self.cache = {}
        

    def get(self, key: int) -> int:
        # if key exist in cache, 
        #     a)  retrieve the value
        #     b)  put the key to the end of the queue
        if key in self.cache:
            value = self.cache[key]
            self.order.remove(key)
            self.order.append(key)
            return value
        
        # if key doesn't exist, return -1
        else:
            return -1


    def put(self, key: int, value: int) -> None:
       
        # if key exist in cache, remove from the cache
        if key in self.cache:
            self.order.remove(key)
            
        # Add the key back to the queue + add key/value in dictionary    
        self.cache[key] = value
        self.order.append(key)
  
        # if the length of queue is greater than capacity, remove the first element       
        if len(self.order) > self.capacity:
            oldest = self.order.popleft()
            del self.cache[oldest]
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
*************************************************************************

class LRUCache2:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = collections.OrderedDict()
      
    def get(self, key: int) -> int:
        if key not in self.cache:
            return - 1
        
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last = False)
        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
    
    
    
class LRUCache3:
    
    def __init__(self, cache: Dict[int, int], capacity: int):
        self.cache = cache
        self.capacity = capacity
        
    
    #1. if no key, return -1 
    #2. delete the key and add it back
    def get(self, key) -> int:
        
        if key not in self.cache:
            return -1
        else:
            tmp = self.cache[key]
            self.cache.pop(key)
            self.cache[key] = tmp
            
    def put(self, key:int , value:int) -> None:
        
        if key in self.cache:
            tmp = self.cache[key]
            self.cache.pop(key)
            self.cache[key] = tmp
            
        elif len(self.cache) == self.capacity:
            self.cache.popitem()
            self.cache[key] = value
        
        else:
            self.cache[key] = value
