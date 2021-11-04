class Solution1:
    def kthFactor(self, n: int, k: int) -> int:
        tmp = []
        for i in range(1, n+1):
            if n%i == 0:
                tmp.append(i)

        if len(tmp) >= k:        
            return tmp[k-1]

        else:
            return -1
                
class Solution2:
    def kthFactor(self, n: int, k: int) -> int:
        
        output = []
        sqrt_n = int(n**0.5)
        
        for index in range(1, sqrt_n+1):
            if n % index == 0:
                output.append(n//index)
                k -= 1
                
                if k == 0:
                    return index
            
        if output[-1]**2== n:
            output.pop()

        if len(output) < k:
            return -1
        
        else:
            return output[-k]
