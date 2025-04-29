class Solution1:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res, combinations = [], []

        def backtrack(i, curr_sum):
            if curr_sum == target:
                res.append(combinations[:])
                return

            if i == len(candidates) or curr_sum > target:
                return

            combinations.append(candidates[i])
            backtrack(i, curr_sum + candidates[i])
            combinations.pop()

            backtrack(i + 1, curr_sum)

        backtrack(0, 0)

        return res

class Solution2:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res, combinations = [], []

        def backtrack(i, remaining):
            if remaining == 0:
                res.append(combinations[:])
                return

            if i == len(candidates) or remaining < 0:
                return

            combinations.append(candidates[i])
            backtrack(i, remaining - candidates[i])
            combinations.pop()

            backtrack(i + 1, remaining)

        backtrack(0, target)

        return res
