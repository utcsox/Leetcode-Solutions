class Solution1:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # if the length of list is equals to k return the original list
        if len(nums) == k:
            return nums
        
        #  Use counter data structure to store the count of each integer       
        counter = collections.Counter(nums)
        
        # use a heapq 
        heap = [(-value, key) for key, value in counter.items()]
        klargest = heapq.nsmallest(k, heap)
        klargest =[ key for value, key in klargest]
        #print(heapq.nlargest(k, counter.keys(), key=counter.get))
        
        return klargest 
    
class Solution2:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # if the length of list is equals to k return the original list
        if len(nums) == k:
            return nums
        
        #  Use counter data structure to store the count of each integer       
        counter = collections.Counter(nums)
        
        # Sort the counter object by value
        result = [] 
        result = list(sorted(counter.items(), key=lambda x: x[1], reverse=True))
        
        # store the top k results
        result= [x[0] for x in result]
        
        return result[:k]
