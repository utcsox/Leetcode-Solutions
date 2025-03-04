class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        counts = collections.Counter(nums)
        nums_sum = sum(nums)
        outlier = float("-inf")

        for num in nums:
            nums_sum -= num
            counts[num] -= 1

            if nums_sum % 2 == 0 and counts[nums_sum // 2] > 0:
                outlier = max(outlier, num)
            nums_sum += num
            counts[num] += 1

        return outlier
