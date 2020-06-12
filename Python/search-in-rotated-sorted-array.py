class Solution1:
    def search(self, nums: List[int], target: int) -> int:
        def find_rotate_index(left, right):
            if nums[left] < nums[right]:
                return 0
            
            while left <= right:
                pivot = (left + right)//2
                if nums[pivot] >  nums[pivot+1]:
                    return pivot + 1
                else:
                    if nums[pivot] < nums[left]:
                        right = pivot - 1
                    else:
                        left = pivot +1
                        
        def binary_search(left, right):
            while left <= right:
                pivot = (left + right) // 2
                if nums[pivot] == target:
                    return pivot
                else:
                    if target < nums[pivot]:
                        right = pivot -1
                    else:
                        left= pivot + 1
            return -1
                        
        n = len(nums)
        if n == 0:
            return -1
        if n == 1:
            return 0 if nums[0] == target else -1
            
        rotate_index = find_rotate_index(0, n-1)
        if nums[rotate_index] == target:
            return rotate_index
                
        if rotate_index == 0:
            return binary_search(0, n-1)
        
        if target < nums[0]:
            return binary_search(rotate_index, n-1)
        
        return binary_search(0, rotate_index)
   
class Solution2:

    def search(self, nums: List[int], target: int) -> int:

        #sortednums = sorted(nums)

        beg, end = 0 , len(nums)-1

        while beg <= end:

            mid = (beg + end)//2

           

            if nums[mid] == target:

                return mid

           

            # if mid point is larger and equals to the beginning element of the array

                 # + if target in between nums[start] & nums[mid]

                 # + if target is greater than nums[start] & nums[mid]

                   

            if nums[beg] <= nums[mid]:

                if target < nums[mid] and target >= nums[beg]:

                    end = mid-1

                else:

                    beg = mid + 1                 

            # if midpoint is less than the beg element of the array

                 # + if target is in beteen Nums[mid] and nums[end]

                 # + if target is less than both nums[mid] and nums[end]

                   

            else:

                if target<= nums[end] and target > nums[mid]:

                    beg = mid+1

                else:

                    end = mid-1

           

        return -1


