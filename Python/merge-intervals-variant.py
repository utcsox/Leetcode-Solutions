class Solution:
    def merge_variant(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:

      res = []
      a, b = 0, 0

      while a < len(A) and b < len(B):
        startFirst, endFirst = A[a]
        startSecond, endSecond = B[b]

        if startFirst <= startSecond:
          self.merge(res, A[a])
          a += 1

        else:
          self.merge(res, B[b])
          b += 1

      if a < len(A):
        while a < len(A):
          startA, endA = A[a]
          self.merge(res, A[a])
          a += 1

      if b < len(B):
        while b < len(B):
          startB, endB = B[b]
          self.merge(res, B[b])
          b += 1
    
      return res

    def merge(self, result, interval):
      if not result or interval[0] > result[-1][1]:
        result.append(interval)
      else:
        result[-1][1] = max(interval[1], result[-1][1]) 

    
    def try_merge(self, result, curr_interval):
      if not result or curr_interval[0] > result[-1][1]:
        result.append(curr_interval)
      else:
        result[-1][1] = max(curr_interval[1], result[-1][1])

def test_merge_variant():
  
  solution = Solution()
  A = [[3, 11], [14, 15], [18, 22], [23, 24], [25, 26]]
  B = [[2, 8], [13, 20]]
  expected = [[2, 11], [13, 22], [23, 24], [25, 26]]
  assert expected == solution.merge_variant(A, B)

  A = []
  B = [[2, 8], [13, 20]]
  expected = [[2, 8], [13, 20]]
  assert expected == solution.merge_variant(A, B)

  A = [[1, 5], [10, 15], [20, 25]]
  B = [[5, 10], [15, 20]]
  expected = [[1, 25]]
  assert expected == solution.merge_variant(A, B)

  A = [[1, 5], [11, 15], [21, 25]]
  B = [[6, 10], [16, 20]]
  expected = [[1, 5], [6, 10], [11, 15], [16, 20], [21, 25]]
  assert expected == solution.merge_variant(A, B)
