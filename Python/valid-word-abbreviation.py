class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        abbr_pt, count = 0, 0

        while abbr_pt < len(abbr):
            # invalid case
            if abbr[abbr_pt] == "0" or count >= len(word):
                return False
            
            # Handle numeric case
            number = ""

            while abbr_pt < len(abbr) and abbr[abbr_pt].isdigit():
                number += abbr[abbr_pt]
                abbr_pt += 1

            if number:
                count += int(number)

            else:
                if abbr[abbr_pt] != word[count]:
                    return False
                count += 1
                abbr_pt += 1

        return count == len(word)
