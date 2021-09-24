class Solution:
    def countAndSay(self, n: int) -> str:
        
        result = '1'
        
        for i in range(n-1):
            tmp, count = '', 1
            
            for j in range(len(result)-1):
                if result[j] == result[j+1]:
                    count +=1
                    
                else:
                    tmp += str(count) + result[j]
                    count = 1
                    
            tmp += str(count) + result[-1]
            result = tmp
            
        return result
