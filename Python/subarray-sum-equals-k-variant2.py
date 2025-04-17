class Solution:
    def subarraySumExistsPositiveNums(self, nums: list[int], k: int) -> bool:

        left, prefix_sum = 0, 0

        for right, num in enumerate(nums):
            prefix_sum += num

            while prefix_sum > k:
                prefix_sum -= nums[left]
                left += 1

            if prefix_sum == k:
                return True

        return False

def test_subarraySumExistsPositiveNums():
    solution = Solution()
    assert solution.subarraySumExistsPositiveNums([1, 1, 1], 2)
    assert solution.subarraySumExistsPositiveNums([1, 2, 3], 3)

    # SubarraySum_SecondVariant True
    assert solution.subarraySumExistsPositiveNums([1, 1, 1], 2) == True
    assert solution.subarraySumExistsPositiveNums([1, 2, 3], 3) == True
    assert solution.subarraySumExistsPositiveNums([1, 2, 3, 1, 1, 1], 5) == True
    assert solution.subarraySumExistsPositiveNums([1, 2, 3, 1, 1, 1], 9) == True
    assert solution.subarraySumExistsPositiveNums([5], 5) == True
    assert solution.subarraySumExistsPositiveNums([5], 10) == False
    assert solution.subarraySumExistsPositiveNums([23, 5, 4, 7, 2, 11], 20) == True
    assert solution.subarraySumExistsPositiveNums([1, 3, 5, 23, 2], 8) == True
    assert solution.subarraySumExistsPositiveNums([4, 2, 5, 2, 6, 1], 9) == True
    assert solution.subarraySumExistsPositiveNums([1, 1, 1, 1, 1, 1], 1) == True
    assert solution.subarraySumExistsPositiveNums([1], 1) == True

    # SubarraySum_SecondVariant False
    assert solution.subarraySumExistsPositiveNums([1, 1, 1], 4) == False
    assert solution.subarraySumExistsPositiveNums([1, 2, 3, 4, 5, 6, 7], 100) == False
    assert solution.subarraySumExistsPositiveNums([100, 101, 102, 103], 2) == False
    assert solution.subarraySumExistsPositiveNums([1, 3, 5, 23, 2], 7) == False

test_subarraySumExistsPositiveNums()
