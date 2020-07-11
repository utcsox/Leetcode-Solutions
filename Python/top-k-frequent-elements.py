class Solution:
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
    
