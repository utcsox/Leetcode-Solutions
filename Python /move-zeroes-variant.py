def move_zeroes_to_front(nums):
    """
    Moves all zeroes in the given list to the front, maintaining the relative order of non-zero elements.

    Args:
        nums: A list of integers.
    """
    swap_index = len(nums) - 1
    for i in range(len(nums) - 1, -1, -1):
        if nums[i] != 0:
            nums[i], nums[swap_index] = nums[swap_index], nums[i]
            swap_index -= 1

def test_move_zeroes_to_front():
    nums = [1, 3, 12, 0, 0, 0]
    move_zeroes_to_front(nums)
    expected = [0, 0, 0, 1, 3, 12]
    assert nums == expected

    nums = [0, 1, 0, 3, 12, 0]
    move_zeroes_to_front(nums)
    expected = [0, 0, 0, 1, 3, 12]
    assert nums == expected

    nums = [1, 3, 12, 0, 0, 0, 0, 0, 0]
    move_zeroes_to_front(nums)
    expected = [0, 0, 0, 0, 0, 0, 1, 3, 12]
    assert nums == expected

    nums = []
    move_zeroes_to_front(nums)
    assert not nums

    nums = [0]
    move_zeroes_to_front(nums)
    expected = [0]
    assert nums == expected

    nums = [0, 0, 0]
    move_zeroes_to_front(nums)
    expected = [0, 0, 0]
    assert nums == expected

    nums = [1, 0, 3, 0, 12]
    move_zeroes_to_front(nums)
    expected = [0, 0, 1, 3, 12]
    assert nums == expected

    nums = [1, 2, 3, 4, 5]
    move_zeroes_to_front(nums)
    expected = [1, 2, 3, 4, 5]
    assert nums == expected

    nums = [0, 0, 3, 4, 5]
    move_zeroes_to_front(nums)
    expected = [0, 0, 3, 4, 5]
    assert nums == expected

test_move_zeroes_to_front()
