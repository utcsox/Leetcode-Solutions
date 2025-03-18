class Solution:

  def __init__(self, list_a, list_b):
    self.list_a = list_a
    self.list_b = list_b

  def merge_vectors_88(self, list_a, list_b):

    a_ptr = len(list_a)//2 - 1
    b_ptr = len(list_b) - 1
    merged_ptr = len(list_a) - 1

    while b_ptr >= 0:
      if a_ptr >= 0 and list_a[a_ptr] >= list_b[b_ptr]:
        list_a[merged_ptr] = list_a[a_ptr]
        a_ptr -= 1
      else:
        list_a[merged_ptr] = list_b[b_ptr]
        b_ptr -= 1

      merged_ptr -= 1

    return list_a

def test_merge_vectors_88():
  list_a = [1, 3, 0, 0]
  list_b = [4, 10]
  expected = [1, 3, 4, 10]
  expected = Solution(list_a=list_a, list_b=list_b).merge_vectors_88(list_a, list_b)
  assert expected == list_a

  list_a = [5, 6, 7, 8, 0, 0, 0, 0]
  list_b = [1, 2, 3, 4]
  expected = [1, 2, 3, 4, 5, 6, 7, 8]
  expected = Solution(list_a=list_a, list_b=list_b).merge_vectors_88(list_a, list_b)
  assert expected == list_a

  list_a = [0]
  list_b = [99]  # Not quite 2N size but algo works!
  expected = [99]
  expected = Solution(list_a=list_a, list_b=list_b).merge_vectors_88(list_a, list_b)
  assert expected == list_a

  list_a = [1, 10, 0, 0]
  list_b = [2, 11]
  expected = [1, 2, 10, 11]
  expected = Solution(list_a=list_a, list_b=list_b).merge_vectors_88(list_a, list_b)
  assert expected == list_a

test_merge_vectors_88()
