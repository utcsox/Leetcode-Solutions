class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        table_lookup = {}
        
        # Create a lookup dictionary
        for index, char in enumerate(order):
            table_lookup[char] = index
        
        # loop thru the words list     
        for index in range(len(words)-1):
            first_word = words[index]
            second_word = words[index + 1]
            
            for j in range(min(len(first_word), len(second_word))):
                if first_word[j] != second_word[j]:
                    # table lookup
                    if table_lookup[first_word[j]] > table_lookup[second_word[j]]:
                        return False
                    break
            else:
                if len(first_word) > len(second_word):
                    return False
                
        return True
