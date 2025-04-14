You are given the root of a binary tree containing digits from 0 to 999 only.

Each root-to-leaf path in the tree represents a number.

For example, the root-to-leaf path 10 -> 88 -> 555 represents the number 1088555. Return the total sum of all root-to-leaf numbers. Test cases are generated so that the answer will fit in a 32-bit integer.

A leaf node is a node with no children.

Example 1:

Input: root = [15,4,125] Output: 25 Explanation: The root-to-leaf path 15->4 represents the number 154. The root-to-leaf path 15->125 represents the number 15125. Therefore, sum = 154 + 15125 = 15279.
