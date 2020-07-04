class Solution1:
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

class Solution2:
    def addStrings(self, num1: str, num2: str) -> str:
        
        # perform addition using unicode representation
        # 1. reverse both strings
        # 2. perform bit by bit addition 
        #.   a)  value = (a + b + carry) % 10
        #    b). carry = (a + b + carry) //10
        
        num1 = num1[::-1]
        num2 = num2[::-1]
        
        p1, p2 = 0, 0
        carry, result = 0, []
        
        while ((p1 < len(num1)) and (p2 < len(num2))):
            cp1 = ord(num1[p1]) - ord('0')
            cp2 = ord(num2[p2]) - ord('0')
            value = (cp1 + cp2 + carry) %10
            carry = (cp1 + cp2 + carry) //10
            result.append(value)
            
            p1 += 1
            p2 += 1
            
        # if there is more digit in p1 or p2 
        if p1 < len(num1):
            while (p1 < len(num1)):
                cp1 = ord(num1[p1]) - ord('0')
                value = ( cp1+ carry) %10
                carry = (cp1 + carry) //10
                result.append(value)
                p1 += 1

        elif p2 < len(num2):
            while (p2 < len(num2)):
                cp2 = ord(num2[p2]) - ord('0')
                value = ( cp2+ carry) %10
                carry = (cp2 + carry) //10
                result.append(value)
                p2 += 1
                
        # if there is still a carry bit 
        if carry == 1 and (p1 == len(num1)) and (p2 == len(num2)):
            result.append(carry)
            
        return ''.join(str(x) for x in result[::-1])
