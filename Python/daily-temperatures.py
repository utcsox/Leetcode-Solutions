class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        output, stack = [0 for i in range(len(temperatures))], []
        
        for curr_date, tmp in enumerate(temperatures):
            
            while stack and temperatures[stack[-1]] < tmp:
                
                prev_date = stack.pop()
                output[prev_date] = curr_date - prev_date
                    
            stack.append(curr_date)
              
        return output
