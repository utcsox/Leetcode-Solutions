class Solution1:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
    
        res = [-1 for index in range(len(nums1))]
        lookup = {num: index for index, num in enumerate(nums1)}

        for i, num2 in enumerate(nums2):
            if num2 in lookup:
                idx = lookup[num2]
                for j in range(i + 1, len(nums2)):
                    if nums2[j] > num2:
                        res[idx] = nums2[j]
                        break

        return res

class Solution2:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
    
        res = [-1 for index in range(len(nums1))]
        lookup = {num: index for index, num in enumerate(nums1)}
        stack = []

        for num in nums2:
            while stack and num > stack[-1]:
                val = stack.pop()
                idx = lookup[val]
                res[idx] = num

            if num in lookup:
                stack.append(num)

        return res
View less
 

