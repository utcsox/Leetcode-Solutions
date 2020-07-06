class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:    
        # 1. create a lookup dictionary of the order of character
        lookup = {char: index for index, char in enumerate(order)}
        print(lookup)
        
        # 2. compare two words, characters by characterz.
        # 3.  when first/second characters are different:
        #     a). if first word char < second word char ->break
        #    b). else first word char > second word char -> return False
        # 4.  When the loop is complete, if the first word is longer than second world - > return False
        # 5.  Return True out of for loop
    
        for index in range(len(words)-1):
            first = words[index]
            second = words[index + 1]
            
            for j in range(min(len(first), len(second))):
                if first[j] != second[j]:
                   
                    if lookup[first[j]] > lookup[second[j]]:
                        print(j, 'adotheo')
                        return False
                    
                    break
            else:
                if len(first) > len(second):
                    return False
                
        return True
