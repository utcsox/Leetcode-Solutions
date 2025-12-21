class Solution1:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        res = [-1 for i in range(len(nums))]
        
        for i in range(len(nums)):
            for j in range(1, len(nums)):
                if nums[(i + j) % len(nums)] > nums[i]:
                    res[i] = nums[(i + j) % len(nums)]
                    break

        return res

class Solution2:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        res = [-1 for i in range(len(nums))]

        stack = []

        for i in range(len(nums) * 2):
            idx = i % len(nums)
            while stack and nums[idx] > nums[stack[-1]]:
                j = stack.pop()
                res[j] = nums[idx]

            if i < len(nums):
                stack.append(i)

        return res 
