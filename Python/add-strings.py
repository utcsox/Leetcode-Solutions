class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        lookup = {
            '0': 0,
            '1': 1,
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 7,
            '8': 8,
            '9': 9
        }
        
        first, second = 0, 0
        for num in num1:
            first = 10*first + lookup[num]
            
        for num in num2:
            second = 10*second + lookup[num]
            
        return str(first+second)
