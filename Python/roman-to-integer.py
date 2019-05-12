class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        symbols = {'I': 1,
                   'V': 5,
                   'X': 10,
                   'L': 50,
                   'C': 100,
                   'D': 500,
                   'M': 1000}
        for index, char in enumerate(s):
            if index <= len(s)-2:

                if (symbols[s[index + 1]] > symbols[s[index]]):

                   result -= symbols[s[index]]
                else:
                    result += symbols[char]
            else:

                result+= symbols[char]

        return result
