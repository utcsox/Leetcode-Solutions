def prevPermutation_31(nums):
    """
    Finds the previous permutation of a given list of integers.

    Args:
        nums: A list of integers.
    """

    k = -1

    for index in range((len(nums) - 1)):
      if nums[index] > nums[index + 1]:
        k = index

    if k == -1:
      nums.reverse()
      return

    sindex = 0

    for index in range(k + 1, len(nums)):
      if nums[index] < nums[k]:
        sindex = index

    nums[k], nums[sindex] = nums[sindex], nums[k]
    nums[k+1: ] = reversed(nums[k+1: ])


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
