class SparseVector:
    def __init__(self, nums: List[int]):
        
        self.dict = {}
        
        for index, num in enumerate(nums):
            self.dict[index] = num
        

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        output = 0
        for k, v in self.dict.items():
            if k in vec.dict:
                output +=  v *vec.dict[k]
                
        return output
                
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
