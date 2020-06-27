class Solution:
    def myAtoi(self, str: str) -> int:
        
        # a) string is empty
        # b) # is greater than 2**31-1
        # c) # is smaller than -2**31
        
        INT_MIN = -2**31
        INT_MAX = 2**31 -1
        result = ''
        
        
        # get the strig strip out of white space and return a list of string
        string = str.strip().split()
        if len(string) == 0:
            return 0
            
        # first sequene    
        first_sequence = string[0]
                
        # optional initial plus or minus sign,
        # initialize sign = 1 if there is no sign indicator
        # if first digit in the first sequence not in '.0123456789', not valid
        
        sign = 1
 
        if first_sequence[0] == '-':
            sign = -1
            
        elif first_sequence[0] == '+':
            sign = 1
        
        elif first_sequence[0] not in '.0123456789':
            return 0
        
        # going to loop thru the string, skip the initial +/- sign
        for index in range(len(first_sequence)):
            if index == 0 and first_sequence[index] in '+-':
                continue
            elif first_sequence[index] not in '.1234567890':
                break
            else:
                result = result +  first_sequence[index]
        
        # if string is empty, return 0
        # check whether result is greater or less than INT_MIN or INT_MAX
        if len(result) == 0:
            return 0
        
        result = int(float(result)) * sign
        
        if result > INT_MAX:
            return INT_MAX
        
        elif result < INT_MIN:
            return INT_MIN
        
        else:
            return result
