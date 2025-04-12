class Solution:
    def findKthPositive(self, arr: list[int], k: int) -> int:
        left = 0
        right = len(arr) - 1
        while left <= right:
            mid = (right - left) // 2 + left
            missing = arr[mid] - arr[0] - mid
            if missing < k:
                left = mid + 1
            else:
                right = mid - 1

        return arr[0] + k + right

solution = Solution()
solution.findKthPositive(arr=[1, 2, 3, 4], k = 2)
