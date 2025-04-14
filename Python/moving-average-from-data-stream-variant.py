class Solution:
  def compute_running_sum_variant_346(self, nums, size):
      """
      Computes the running average of subarrays of a given size.

      Args:
          nums: A list of integers.
          size: The size of the subarray.

      Returns:
          A list of integers representing the averages of each subarray.
      """
      res = [] 
      window_sum = 0
      left = 0 

      for right in range(len(nums)):
        if right - left + 1 <= size:
          window_sum += nums[right]
          if right - left + 1 == size:
            res.append(window_sum // size)
            window_sum -= nums[left]
            left += 1

      return res

def test_compute_running_sum_variant_346():
    solution = Solution()
    nums = [5, 2, 8, 14, 3]
    k = 3
    expected = [5, 8, 8]
    assert expected == solution.compute_running_sum_variant_346(nums, k)

    nums = [6]
    k = 1
    expected = [6]
    assert expected == solution.compute_running_sum_variant_346(nums, k)

    nums = [1, 2, 3]
    k = 1
    expected = [1, 2, 3]
    assert expected == solution.compute_running_sum_variant_346(nums, k)

test_compute_running_sum_variant_346()
