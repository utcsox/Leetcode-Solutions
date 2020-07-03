class Solution1:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        for index in range(m, m+n):
            nums1[index]= nums2[i]
            i = i + 1
        nums1.sort()
        
        
 class Solution2:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # two pointer solution
        #1. make a copy of nums1
        #2. merge nums1 and nums2
        
        copy = nums1[:m]
        nums1[:] = []
        p1, p2 = 0, 0
        
        while p1<m and p2<n:
            if copy[p1] < nums2[p2]:
                nums1.append(copy[p1])
                p1 += 1
                
            else:
                nums1.append(nums2[p2])
                p2 += 1
                
        if p1< m:
            nums1[p1+p2: ] = copy[p1:]
            
        else:
            nums1[p1+p2:] = nums2[p2:]
