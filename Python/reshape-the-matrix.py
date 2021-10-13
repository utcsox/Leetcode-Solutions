class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        
        tmp = []
        for element in mat:
            tmp.extend(element)
            
        if len(tmp) != r *c:
            return mat
        
        output = []
        
        for i in range(r):
            output.append(tmp[i*c: i*c+c])
            
        return output
