class Solution:
    def find_valley_element(self, nums: List[int]) -> int:

      left, right = 0, len(nums) - 1
      while left <= right:
          mid = (left + right) // 2
          if nums[mid - 1] < nums[mid] and mid > 0:
            right = mid - 1
          elif nums[mid + 1] < nums[mid] and mid < len(nums) - 1:
            left = mid + 1
          else:
            return mid
            
def test_find_valley_element():
  solution = Solution()
  nums = [1, 2, 3, 1]
  solution.find_valley_element(nums)
  assert solution.find_valley_element(nums) == 0

  nums = [1, 2, 3, 5, 3, 4, 3, 1, 6]
  assert solution.find_valley_element(nums) == 4

  nums = [3, 2, 3, 4, 3, 2]
  assert solution.find_valley_element(nums) == 1

  nums = [1, 2, 3, 4, 3, 2]
  assert solution.find_valley_element(nums) == 0
