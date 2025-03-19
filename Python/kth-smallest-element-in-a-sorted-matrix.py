class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:

        left, right = matrix[0][0], matrix[-1][-1]

        def count_less_equal(mid):
            count = 0
            for row in matrix:
                count += bisect.bisect_right(row, mid)
            return count
        
        while left < right:
            mid = (left + right) // 2

            if count_less_equal(mid) < k:
                left = mid + 1

            else:
                right = mid

        return left
