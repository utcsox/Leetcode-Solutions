class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        # in-place sort of the array.
        
        result = []
        if not nums:
            return result 
        nums.sort()
        index = 0
        
        while index < len(nums)-2:  
            # after the first element, if the value of next element is the same as the previous one,
            # we want to skip it
            
            if (index > 0 and nums[index] == nums[index-1]):
                index += 1
                continue
            
            else:
                
                low, high = index+1, len(nums)-1

                while low < high:

                    # calculate the sum of three values
                    # if it is < 0, we increment the low pointer
                    # if it is > 0, we decrement the high pointer
                    # if it is equal to 0, we add it to the result

                    total = nums[index] + nums[low] + nums[high]

                    if total < 0:
                        low += 1
                    elif total > 0:
                        high -= 1

                    else:

                        result.append([nums[index], nums[low], nums[high]])
                        low += 1
                        high -= 1

                        # we want to check if the next element has the same value of:           
                        # nums[low]/nums[high]          
                        # increase/decrease the pointer if it is true

                        while low < high and nums[low] == nums[low - 1]:
                            low += 1

                        while low < high and nums[high] == nums[high + 1]:
                            high -= 1

            index = index + 1


        return result
