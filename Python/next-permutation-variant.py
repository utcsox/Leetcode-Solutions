def prevPermutation_31(nums):
    """
    Finds the previous permutation of a given list of integers.

    Args:
        nums: A list of integers.
    """

    pivot = -1

    for index in range((len(nums) - 1)):
      if nums[index] > nums[index + 1]:
        pivot = index

    if pivot == -1:
      nums.reverse()
      return

    swap = 0

    for index in range(pivot + 1, len(nums)):
      if nums[index] < nums[pivot]:
        swap = index

    nums[pivot], nums[swap] = nums[swap], nums[pivot]
    nums[pivot + 1: ] = reversed(nums[pivot + 1: ])


def test_prevPermutation_31():
    nums = [3, 2, 1]
    expected = [3, 1, 2]
    prevPermutation_31(nums)
    assert expected == nums

    nums = [1, 2, 3]
    expected = [3, 2, 1]
    prevPermutation_31(nums)
    assert expected == nums

    nums = [9, 6, 5, 4, 3, 2]
    expected = [9, 6, 5, 4, 2, 3]
    prevPermutation_31(nums)
    assert expected == nums

    nums = [4, 5, 1, 1, 3, 7]
    expected = [4, 3, 7, 5, 1, 1]
    prevPermutation_31(nums)
    assert expected == nums

test_prevPermutation_31()
