class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        set1 = set(nums1)
        set2 = set(nums2)
        
        return(list(set1.intersection(set2)))
        
        #return list(set([num for num in nums1 if num in nums2]))