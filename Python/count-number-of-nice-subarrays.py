class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:

        result = 0
        #1.  Find the index of with odd number
        ind = [k for k, v in enumerate(nums) if v%2==1]
        
        #2.  loop thru the array
        
        0, 1, 2, 3, 4, 5
        for index in range(len(ind)-k+1):
            left = ind[index]  
            right = ind[index+k -1]
            
            if index > 0:
                outer_left = ind[index-1]
            else:
                outer_left = -1
                
            if (index + k) < len(ind):
                outer_right = ind[index+ k]
                
            else:
                outer_right = len(nums)
                
            result += (left - outer_left) * (outer_right - right)
            
            
        return result
