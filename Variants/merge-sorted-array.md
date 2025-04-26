You are given two integer arrays `list_a` and `list_b`, sorted in **no-decreasing order**.

Merge `list_a` and `list_b` into a single array sorted in **non-decreasing order**.

The final sorted array should not be returned by the function, but instead sorted inside the array `list_a`.  To accomondate this,
`list_a` is double the length of `list_b`, where the first half of elements denote the elments that should be merged, and the 
last half of elements are set to 0 and should be ignored.

**Example 1**:
  Input:  list_a = [1, 8, 0, 0], list_b = [3, 5]
  Output: [1, 3, 5, 8]
  Explanation:  The arrays we are merging are [1, 8] and [3, 5]

  The result of the merge is [1, 3, 5, 8] with the underlined elements coming from list_a
