class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        start, max_ones = 0, 0

        for end, num in enumerate(nums):
            if num == 0:
                k -= 1

            if k < 0:
                if nums[start] == 0:
                    k += 1
                start += 1   
            else:
                max_ones = max(max_ones, end - start + 1)

        return max_ones
