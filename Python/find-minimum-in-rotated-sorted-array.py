class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        if len(nums)==1:
            return nums[0]
        left, right = 0 , len(nums)-1
        
        #1.  if array has not rotated, last element > first element
        #.   return the first element as min
        if nums[right] > nums[left]:
                return nums[left]
            
        while left <= right:
            mid = (left + right)//2
   
        #2.  If find the inflection point, return the point after the inflection point   
            if nums[mid] > nums[mid+1]:
                return nums[mid+1]
            
        #3 a) if inflection point > first element of the array, the inflection point must be on the                   right side of the mid point
        #  b). if inflection point < first element of the array, the inflection must be on the left                    side of the mid point 
            else:
                if nums[mid] < nums[left]:
                    right = mid-1
                    
                else:
                    left = mid+1
                    
        return -1
        
