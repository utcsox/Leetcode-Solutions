class Solution:
    def myAtoi(self, str: str) -> int:
              
        INT_MAX =  2147483647
        INT_MIN = -2147483648
        result = ''
        sign = 1
        
        str = str.strip().split()
        if len(str)==0: return 0
        first = str[0]
        print(first)
        
        if first[0] == '-':
            sign = -1
        elif first[0] == '+':
            sign = 1
        elif first[0] not in '.0123456789':
                return 0
        for i in range(len(first)):
            if i == 0 and first[i] in "-+":
                continue
            elif first[i] not in '.0123456789':
                break
            else:
                result += first[i]
       
        if len(result) == 0:
            return 0
        result = int(float(result))*sign
        print(result, type(result))

        if result > INT_MAX:
            return INT_MAX
        elif result < INT_MIN:
            return INT_MIN
        elif isinstance(result, int) :
            return result
