class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        
        for token in tokens:
            
            if token not in "+-*/":
                stack.append(token)
                
            else:
                result = 0
                num1 = int(stack.pop())
                num2 = int(stack.pop())
                
                if token == '+':
                    result = num2 + num1
                    
                elif token == '-':
                    result = num2 - num1
                    
                elif token == '*':
                    result = num2 * num1
                    
                else:
                    result = int(num2/num1)
                    
                stack.append(result)
                    
                    
        return stack.pop()   
