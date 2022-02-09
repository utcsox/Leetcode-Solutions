class Solution:
    def countBits(self, n: int) -> List[int]:
        output =[0]*(n+1)
        
        
        for num in range(n+1):
            count = 0
            tmp = num
            
            while tmp > 0:
                count += tmp & 1
                tmp = tmp >> 1
                
            output[num] = count
            
        return output
