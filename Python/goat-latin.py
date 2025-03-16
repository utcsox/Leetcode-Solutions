class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
        split_sentence = sentence.split()
        output = []

        for i, word in enumerate(split_sentence):
            curr_word = ""
            first_char = word[0]
            if first_char not in vowels:
                curr_word = word[1:] + first_char
            else:
                curr_word = word 
            curr_word += "ma"
            
            curr_word = curr_word + (i+1)*"a"
            output.append(curr_word)

        return " ".join(output)
