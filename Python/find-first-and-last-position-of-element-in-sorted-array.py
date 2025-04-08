class Solution1:
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

class Solution2:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        start, end = -1, -1
        l = bisect.bisect_left(nums, target)
        r = bisect.bisect_right(nums, target)

        if l < len(nums) and nums[l] == target:
            start = l

        if nums[r - 1] == target:
            end = r - 1

        return[start, end]
