class Solution:
    def topKeyword(self, reviews: List[int], keywords, k: int) -> List:
        
        kword = defaultdict(int)
        for review in reviews:
            temp = set(review.lower().split())
            for word in temp:
                if word in keywords:
                    kword[word] += 1
        
        counter = Counter(kword)
        
        lookup = defaultdict(list)
        
        for key, value in counter.items():
            lookup[value].append(key)
            
        for key in lookup:
            lookup[key].sort()
        
        lookup_list = list(sorted(lookup.items()))
        
        print(lookup_list)
        for item in lookup_list:
            print(item)
            
        
        output = [x[1][0] for x in lookup_list]
        
        return output[len(output)-k:]
