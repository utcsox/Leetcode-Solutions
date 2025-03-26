class Solution1:
    def findKthPluseOneLargest(self, nums: List[int], k: int) -> int:

        if k + 1 > len(nums):
            return 0

        return heapq.nlargest(k + 1, nums)[k]

  class Solution2:
    def findKthPluseOneLargest(self, nums: List[int], k: int) -> int:

        if k + 1 > len(nums):
            return 0

        k = k + 1

        heap = []

        for num in nums:
          if len(heap) < k:
            heapq.heappush(heap, num)

          else:
            if num > heap[0]:
              heapq.heappop(heap)
              heapq.heappush(heap, num)

        return heap[0]

    def test_findKthPluseOneLargest():
  solution = Solution()
    # Distinct elements in nums
  nums = [1, 2, 3, 4, 5]
  k = 0
  assert solution.findKthPluseOneLargest(nums, k) == 5
  k = 1
  assert solution.findKthPluseOneLargest(nums, k) == 4
  k = 2
  assert solution.findKthPluseOneLargest(nums, k) == 3
  k = 3
  assert solution.findKthPluseOneLargest(nums, k) == 2
  k = 4
  assert solution.findKthPluseOneLargest(nums, k) == 1
  
  nums = [1]
  k = 0
  assert solution.findKthPluseOneLargest(nums, k) == 1
  
  # Out of range indices
  nums = [1, 2, 3, 4, 5]
  try:
      solution.findKthPluseOneLargest(nums, 5)
      assert False, "Expected an out_of_range exception"
  except AssertionError:
      pass
  try:
      solution.findKthPluseOneLargest(nums, 50)
      assert False, "Expected an out_of_range exception"
  except AssertionError:
      pass

  nums = [1]
  k = 1
  try:
      solution.findKthPluseOneLargest(nums, k)
      assert False, "Expected an out_of_range exception"
  except AssertionError:
      pass

  # Edge Case: Empty list
  nums = []
  k = 0
  try:
      solution.findKthPluseOneLargest(nums, k)
      assert False, "Expected an out_of_range exception"
  except AssertionError:
      pass
  
  k = 1
  try:
      solution.findKthPluseOneLargest(nums, k)
      assert False, "Expected an out_of_range exception"
  except AssertionError:
      pass

  k = 2
  try:
      solution.findKthPluseOneLargest(nums, k)
      assert False, "Expected an out_of_range exception"
  except AssertionError:
      pass

test_findKthPluseOneLargest()
