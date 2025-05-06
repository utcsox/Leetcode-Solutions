Given a string formed by Integers, find all combinations that sum up to a target.
Using standard integer arithmetic operators +, -, how many different solution can you find by inserting the operators between some digits?

Example 1:
  Input: "123456789" target: 100
  Output: 12

All combinations that sums up to 100:
1 + 2 + 3 - 4 + 5 + 6 + 78 + 9
1 + 2 + 34 - 5 + 67 - 8 + 9
1 + 23 - 4 + 5 + 6 + 78 - 9
1 + 23 - 4 + 56 + 7 + 8 + 9
-1 + 2 - 3 + 4 + 5 + 6 + 78 + 9
12 + 3 + 4 + 5 - 6 - 7 + 89
12 + 3 - 4 + 5 + 67 + 8 + 9
12 - 3 - 4 + 5 - 6 + 7 + 89
123 + 4 - 5 + 67 - 89
123 - 4 - 5 - 6 - 7 + 8 - 9
123 + 45 - 67 + 8 - 9
123 - 45 - 67 + 89
