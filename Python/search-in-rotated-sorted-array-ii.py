class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (right + left) // 2
            if nums[mid] == target:
                return True

            # nums[left] < nums[target] < nums[mid]
            if nums[left] < nums[mid]:
                if nums[left] <= target and target < nums[mid]:
                    right = mid - 1

                else:
                    left = mid + 1

            elif nums[left] > nums[mid]:
                if nums[mid] < target and target <= nums[right]:
                    left = mid + 1

                else:
                    right = mid - 1

            else:
                left += 1

        return False
