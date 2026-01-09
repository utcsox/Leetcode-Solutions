class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0

        l, prod, res = 0, 1, 0

        for r, num in enumerate(nums):
            prod *= num
            while l <= r and prod >= k:
                prod //= nums[l]
                l += 1

            res += r - l + 1

        return res
