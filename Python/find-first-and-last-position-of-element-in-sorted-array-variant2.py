class Solution:
    def countUnique(self, nums: list[int]) -> int:
        # Should run in O(k * log(N)) complexity, where k is # of unique elements
        if len(nums) == 0:
            return 0

        def upper(arr, target):
            left, right, i = 0, len(arr) - 1, -1
            while left <= right:
                mid = (left + right) // 2
                if arr[mid] < target:
                    left = mid + 1
                elif arr[mid] > target:
                    right = mid - 1
                else:
                  i = mid
                  left = mid + 1
            return i

        start = 0
        count = 0
        while start < len(nums):
            end = upper(nums, nums[start])
            start = end + 1
            count += 1

        return count

def test_countUnique():
    solution = Solution()
    # Nonzero Count cases
    nums = [2, 2, 3, 3, 3, 9, 9, 9, 9, 9, 10, 12, 12]
    assert solution.countUnique(nums) == 5
    nums = [-3, -2, -1, 0, 1, 2, 3]
    assert solution.countUnique(nums) == 7
    nums = [-3, -3, -3, -2, -2, -2, -1, -1, -1, 0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3]
    assert solution.countUnique(nums) == 7
    nums = [1, 1, 1, 1, 2, 2, 2, 2, 5, 5, 5, 7, 7, 8, 8, 10]
    assert solution.countUnique(nums) == 6
    nums = [19, 19, 19, 19]
    assert solution.countUnique(nums) == 1
    nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert solution.countUnique(nums) == 1
    nums = [9001]
    assert solution.countUnique(nums) == 1
    nums = [5, 7, 7, 8, 8, 10]
    assert solution.countUnique(nums) == 4
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert solution.countUnique(nums) == 10

    # Zero Count case
    nums = []
    assert solution.countUnique(nums) == 0

test_countUnique()
