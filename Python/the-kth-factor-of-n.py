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
                
