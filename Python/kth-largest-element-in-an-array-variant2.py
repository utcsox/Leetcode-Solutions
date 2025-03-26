class Solution1:
    def findKthSmallest(self, nums: List[int], k: int) -> int:
      heap = []
      for num in nums:
        heapq.heappush(heap, -num)
        if len(heap) > k:
          heapq.heappop(heap)
      return -heap[0]

class Solution2:
    def findKthSmallest(self, nums: List[int], k: int) -> int:
      
        return heapq.nsmallest(k, nums)[k-1]

def test_findKthSmallest():
  solution = Solution()
  assert solution.findKthSmallest([2, 10, 8, 3, 7, 9], 2) == 3
  assert solution.findKthSmallest([2, 10, 8, 3, 7, 9], 4) == 8

  assert solution.findKthSmallest([3, 8, 4, 1, 10], 1) == 1
  assert solution.findKthSmallest([3, 8, 4, 1, 10], 2) == 3
  assert solution.findKthSmallest([3, 8, 4, 1, 10], 3) == 4
  assert solution.findKthSmallest([3, 8, 4, 1, 10], 4) == 8
  assert solution.findKthSmallest([3, 8, 4, 1, 10], 5) == 10

  assert solution.findKthSmallest([1, 1, 1, 1, 2], 1) == 1
  assert solution.findKthSmallest([1, 1, 1, 1, 2], 2) == 1
  assert solution.findKthSmallest([1, 1, 1, 1, 2], 3) == 1
  assert solution.findKthSmallest([1, 1, 1, 1, 2], 4) == 1
  assert solution.findKthSmallest([1, 1, 1, 1, 2], 5) == 2

  assert solution.findKthSmallest([-1, -5, -2, -3, -4], 1) == -5
  assert solution.findKthSmallest([-1, -5, -2, -3, -4], 2) == -4
  assert solution.findKthSmallest([-1, -5, -2, -3, -4], 3) == -3
  assert solution.findKthSmallest([-1, -5, -2, -3, -4], 4) == -2
  assert solution.findKthSmallest([-1, -5, -2, -3, -4], 5) == -1

test_findKthSmallest()
