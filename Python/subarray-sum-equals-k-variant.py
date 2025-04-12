class Solution:
    def subarraySumExists(self, nums: list[int], k: int) -> bool:

      lookup = set([0])

      prefix_sum = 0

      for num in nums:
        prefix_sum += num
        if prefix_sum - k in lookup:
          return True

        lookup.add(prefix_sum)

      return False        

def test_subarraySumExists():
    solution = Solution()
    assert solution.subarraySumExists([1, 1, 1], 2)
    assert not solution.subarraySumExists([1, 4, 7], 3)

    # SubarraySum_FirstVariant True
    assert solution.subarraySumExists([1, 1, 1], 2) == True
    assert solution.subarraySumExists([1, 2, 3, 1, 1, 1], 5) == True
    assert solution.subarraySumExists([1, 2, 3, 1, 1, 1], 9) == True
    assert solution.subarraySumExists([3, 4, 7, 2, -3, 1, 4, 2, 1, -14], 7) == True
    assert solution.subarraySumExists([1, 2, 3, -3, 1, 1], 0) == True
    assert solution.subarraySumExists([1, -3, 3, -3, 3, -3], 0) == True
    assert solution.subarraySumExists([1, -3, 3, -6, 8, -3, 4, 5, 6], 8) == True
    assert solution.subarraySumExists([1, -3, 3, -6, 8, -3, 4, 5, 6], -1) == True
    assert solution.subarraySumExists([5], 5) == True
    assert solution.subarraySumExists([5], 10) == False
    assert solution.subarraySumExists([-1, -2, -3, -4], -5) == True
    assert solution.subarraySumExists([-1, -2, -3, -4], -10) == True
    assert solution.subarraySumExists([0, 0, 0, 0, 0], 0) == True
    assert solution.subarraySumExists([8, 3, 6, 1, -5, 10], 10) == True

    # SubarraySum_FirstVariant False
    assert solution.subarraySumExists([1, 1, 1], 4) == False
    assert solution.subarraySumExists([3, 4, 7, 2, -3, 1, 4, 2, 1, -14], -10) == False
    assert solution.subarraySumExists([-1, -2, -3, -4], -15) == False
test_subarraySumExists()
