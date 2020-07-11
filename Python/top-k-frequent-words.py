class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
         
        #1.  Use the Counter object to get the count of each word 
        count = (collections.Counter(words))
        
        #2.  Create a dictionary object where key = # of times words appear and value = word
        lookup = collections.defaultdict(list)
        
        for key, value in count.items():
            lookup[value].append(key)
        
        #3.  Alphabetically sort the list of each key 
        for key in lookup:
            lookup[key].sort()
        
        #4.  Create the list that sorted by the key 
        lookup_list = list(sorted(lookup.items(), reverse=True))
        
        #5.  Use list concatanation to grab the elements of the lookup_list
        output = [y for x in lookup_list for y in x[1] ]
        
        return output[:k]
        
