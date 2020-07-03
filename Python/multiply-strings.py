class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        return str(int(num1) * int(num2))
        
class Solution2:
  def multiply(self, num1: str, num2: str) -> str:
      num = 0
      for index, element in enumerate(num2[::-1]):
          num += int(num1) * int(element)*10**(index)
      return str(num)

class Solution3:
    def multiply(self, num1: str, num2: str) -> str:
        
        # if either num1 or num2 are empty string, return 0
        if not num1 or not num2:
            return '0'
        
        # create a string to integer dictionary 
        str_num = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

        # convert string to number
        num_1, num_2 = 0, 0
        for index in num1:
            num = str_num[index]
            num_1 = num_1 * 10 + num

        for index in num2:
            num = str_num[index]
            num_2 = num_2 * 10 + num
            
        return str(num_1*num_2)
