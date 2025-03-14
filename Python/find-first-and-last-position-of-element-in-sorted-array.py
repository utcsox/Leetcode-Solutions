class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def binary_search(nums, target, lflag):
            l, r, i = 0, len(nums) - 1, -1
            while l <= r:
                mid = (l + r) // 2
                if target > nums[mid]:
                    l = mid + 1
                elif target < nums[mid]:
                    r = mid - 1
                else:
                    i = mid
                    if lflag:
                        r = mid - 1

                    else:
                        l = mid + 1
            return i

        l = binary_search(nums, target, 1)
        r = binary_search(nums, target, 0)
        return [l, r]
