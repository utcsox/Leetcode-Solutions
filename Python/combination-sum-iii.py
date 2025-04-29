class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res, combinations = [], []

        def backtrack(start, curr_sum):

            if curr_sum == n and len(combinations) == k:
                res.append(combinations[:])
                return

            elif curr_sum > n or len(combinations) == k:
                return

            for i in range(start, 10):
                combinations.append(i)
                backtrack(i + 1, curr_sum + i)
                combinations.pop()

        backtrack(1, 0)

        return res
