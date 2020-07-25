class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        
        output = []
        
        # 1.  add upper to the end of list: nums
        nums.append(upper + 1)
        
        prev = lower - 1
        
        for num in nums:
            
            # if only one element difference, i.e, -1, 0
            if prev + 1 == num:
                prev = num
                continue
            
            # take care:
            # a. elements in nums that are smaller than prev
            # b. current element equals to previous element
            
            if prev >= num:
                continue
                
            start = prev+1
            end = num - 1
            
            # condition that there is a missing element between prev and num
            if start == end:
                output.append(str(start))
                
            else:
                output.append(str(start) + '->' + str(end))
                
            prev = num
            
        return output
            
