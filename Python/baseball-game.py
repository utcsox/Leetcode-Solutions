class Solution:
    def calPoints(self, ops: List[str]) -> int:
        output = []
        for op in ops:               
            if op == '+':
                output.append(output[-1] + output[-2])
                
            elif op == 'D':
                output.append(2*output[-1])
                
            elif op == 'C':
                output.pop()
                
            else:
                output.append(int(op))
                
        return sum(output)
