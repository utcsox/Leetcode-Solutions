class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        #1.  Create a list of tupe value: (num , abs(num-x))
        tmp = []
        for num in arr:
            tmp.append((num, abs(num-x)))
        
        # Create a dictionary store key: abs(num-x), value as a list (num)
        lookup = defaultdict(list)
        for index in tmp:
            lookup[index[1]].append(index[0])
        
        # need to sort the value cause return top K demand smallest # return first
        for key in lookup:
            lookup[key].sort()
         
        #[(0, [1, 2]), (1, ([2, 4]) ]
        lookup_list = list(sorted(lookup.items(), key = lambda x: x[0]))
        
        result = [y for x in lookup_list for y in x[1]][:k]
        result.sort()    
        
        
        return result
