class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        # 1.  create a list of tuples (a, abs(a-x))
        tmp = [(a, abs(a-x)) for a in arr]
        
        # 2.  orted the tuples by first element in the tmp list
        output = sorted(tmp, key = lambda x: x[1])
        
        #3. return the sorted a in the first k element of the output
        return sorted([i[0] for i in output[:k]])
