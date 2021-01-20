class Solution:
    def SparseMatrixMultiplication(self, arr1: List, arr2: List) -> int:
        dict1 = {i: j for i, j in enumerate(arr1) if j != 0} 
        dict2 = {i: j for i, j in enumerate(arr2) if j != 0} 
        product = 0 
        for k, v in dict1.items():
            if k in dict2:
                product +=  v*dict2[k]
        
        return product
