class NumArray:

    def __init__(self, nums: List[int]):
        self.accum = [0]
        for num in nums:
            self.accum.append(self.accum[-1] + num)
        

    def sumRange(self, i: int, j: int) -> int:
        return self.accum[j+1]-self.accum[i]



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
