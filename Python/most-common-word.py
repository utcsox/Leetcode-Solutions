class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        
        # 1. preprocess the string: lower + remove punctuation
        normalized_str = ''.join([c.lower() if c.isalnum() else ' ' for c in paragraph])
        
        # 2.  Split the string into words
        words = normalized_str.split()

        output = defaultdict(int)
        for word in words:
            if word not in banned:
                output[word] += 1
                
        value = [(value, key) for key, value in output.items()]
        
        return max(value)[1]
