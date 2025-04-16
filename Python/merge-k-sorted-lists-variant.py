class Solution:
  def mergeKLists_variant(self, lists: List[Optional[int]]):
      min_heap = []
      for i, lst in enumerate(lists):
          if lst:
              heapq.heappush(min_heap, (lst[0], i, 0))  # (value, list_index, index)
      result = []
      while min_heap:
          val, list_index, index = heapq.heappop(min_heap)
          result.append(val)

          index += 1
          if index < len(lists[list_index]):
              heapq.heappush(min_heap, (lists[list_index][index], list_index, index))

      return result

def test_mergeKLists_variant(): 
  solution = Solution()
  
  lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
  assert solution.mergeKLists_variant(lists) == [1, 1, 2, 3, 4, 4, 5, 6]

  lists = [[1],[0]]
  assert solution.mergeKLists_variant(lists) == [0, 1]

  lists = []
  assert solution.mergeKLists_variant(lists) == []
  
  lists = [[]]
  assert solution.mergeKLists_variant(lists) == []


test_mergeKLists_variant()

