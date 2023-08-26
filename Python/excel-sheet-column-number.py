class Solution:
    def titleToNumber(self, columnTitle: str) -> int:

        lookup = {chr(index + 65): index + 1 for index in range(26)}
        output = 0


        for index in reversed(range(len(columnTitle))):
            output += lookup[columnTitle[index]] * 26 ** (len(columnTitle) - index - 1)

        return output
