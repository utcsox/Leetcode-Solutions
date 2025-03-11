A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

For example, for arr = [1,2,3], the following are all the permutations of arr: [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].
The previous permutation of an array of integers is the previous lexicographically smaller permutation of its integer. More formally, if all the permutations of the array are sorted in one container 
according to their lexicographical order, then the previous permutation of that array is the permutation that precedes it in the sorted container. If such arrangement is not possible, the array must be 
rearranged as the highest possible order (i.e., sorted in ascending order).

For example, the previous permutation of arr = [3,2,1] is [3,1,2].
Similarly, the previous permutation of arr = [1,2,3] is [3,2,1].
The previous permutation of arr = [1,2,3] is [3,2,1] because [1,2,3] does not have a lexicographical smaller rearrangement.
Given an array of integers nums, find the next permutation of nums.

The replacement must be in place and use only constant extra memory.

