class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
    
        res = [-1 for index in range(len(nums1))]
        lookup = {num: index for index, num in enumerate(nums2)}

        for i, num1 in enumerate(nums1):
            if num1 in lookup:
                idx = lookup[num1]
                for j in range(idx + 1, len(nums2)):
                    if nums2[j] > num1:
                        res[i] = nums2[j]
                        break

        return res
