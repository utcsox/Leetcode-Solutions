Given two array intervals A and B where intervals in A have no overlap in A and intervals in B have no overlap in B.  
Furthermore, A[i], B[i] = [start, end], merge all overlapping intervals between the two interval lists, and
return an array of the non-overlapping intervals that cover all the intervals in the input.

Note:  Both A and B are sorted by start in ascending order.

Example 1:
  Input: A = [[3, 11], [14, 15], [18, 22], [23, 24], [25, 26]]
         B = [[2, 8], [13, 20]]

  Output : [[2, 11], [13, 22], [23, 24], [25, 26]]

Example 2:
  Input: A = [], B = [[0, 4], [10, 13]]
  Output: [[0, 4]. [10, 13]]
