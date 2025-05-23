Variant 1:

There are `n` buildings in a line. You are given an integer array `heights` of size `n` that represents the heights of the buildings in the line.

The ocean is to the right of the buildings. A building has an ocean view if the building can see the ocean without obstructions. Formally, a building has an ocean view if all the buildings to its right have a **smaller** height.

Return the number of buildings that have an ocean view, sorted in increasing order.

**Example 1:**

Input: heights = [4,2,3,1]
Output: 3
Explanation: Building 1 (0-indexed) does not have an ocean view because building 2 is taller.
