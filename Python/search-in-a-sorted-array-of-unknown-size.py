# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        left, right = 0, 1
        
        # 1. Search the boundary
        while reader.get(right) < target:
                left = right
                right = left * 2
                
        # binary search
        
        while left <= right:
            mid = left + (right-left)//2
            num = reader.get(mid)
            if reader.get(mid) == target:
                return mid
            
            elif num < target:
                left = mid+1
                
            else:
                right = mid - 1
                
        return -1
