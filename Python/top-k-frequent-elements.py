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
    
 class Solution3:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counter = collections.Counter(nums)
        key_list = list(counter.keys())
        print(key_list)
        
        def partition(i, j):
            pivot_value = counter[key_list[j]] 
            left = i - 1
            
            for right in range(i, j):
                if counter[key_list[right]] < pivot_value:
                    left += 1
                    key_list[left], key_list[right] = key_list[right], key_list[left]
                    
            key_list[left+1], key_list[j] = key_list[j], key_list[left+1]
            
            return left+1
                
        def quickselect(i, j, k):
            if i >= j:
                return
            
            pivot_index = partition(i, j)
            
            if (pivot_index-i + 1) == k:
                return
            
            elif (pivot_index - i + 1) < k:
                quickselect(pivot_index + 1, j, k-(pivot_index-i +1))
                
            else:
                quickselect(i, pivot_index-1, k)
            
            return 0
        
        
        quickselect(0, len(key_list)-1, len(key_list)-k)
        return key_list[len(key_list)-k:]
        
