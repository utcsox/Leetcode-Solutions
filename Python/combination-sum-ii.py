class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res, combination = [], []
        candidates.sort()

        def backtrack(start, curr_sum):
            if curr_sum == target:
                res.append(combination[:])
                return

            if start == len(candidates) or curr_sum > target:
                return

            combination.append(candidates[start])
            backtrack(start + 1, curr_sum + candidates[start])
            combination.pop()

            while start + 1 < len(candidates) and candidates[start] == candidates[start + 1]:
                start += 1
            backtrack(start + 1, curr_sum)

        backtrack(0, 0)

        return res
