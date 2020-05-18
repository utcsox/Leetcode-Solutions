class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        return str(int(num1) * int(num2))
        
class Solution2:
  def multiply(self, num1: str, num2: str) -> str:
      num = 0
      for index, element in enumerate(num2[::-1]):
          num += int(num1) * int(element)*10**(index)
      return str(num)
