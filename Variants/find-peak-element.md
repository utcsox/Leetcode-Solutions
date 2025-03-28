A peak element is an element that is strictly less than its neighbors.

Given a 0-indexed integer array nums, find a valley element, and return its index. If the array contains multiple valleys, return the index to any of the valleys.

You may imagine that nums[-1] = nums[n] = +∞. In other words, an element is always considered to be strictly less than a neighbor that is outside the array.

You must write an algorithm that runs in O(log n) time.

Example 1:

Input: nums = [1,2,3,1]
Output: 0
Explanation: 0 is a valley element and your function should return the index number 0.
