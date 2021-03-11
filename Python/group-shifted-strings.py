class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        
        #1.  Create a default dictionary
        lookup = defaultdict(list)
        
        #2.  Loop thru each words in the input strings
        #3. Get the Unicode difference of subsequence letters
        #4. Get mod(# from step #3 / 26) and add into a temp array
        
        for index, word in enumerate(strings):
            tmp = []
            for j in range(1, len(word)):
                number = (ord(word[j])-ord(word[j-1]))%26
                tmp.append(number)
                
       #5.  Add the word to key with same tmp array         
            lookup[tuple(tmp)].append(word)
            
            
        return list(lookup.values())
